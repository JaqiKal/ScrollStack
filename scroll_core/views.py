# scroll_core/views.py
from django.shortcuts import render
from django.http import (
    HttpResponseForbidden,
    HttpResponseNotFound, HttpResponseServerError, Http404
)
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy
from .forms import SearchForm
from django.db.models import Q 
from django.utils import timezone
from allauth.account.views import PasswordResetFromKeyView







# Simple function-based view for the index page
def index(request):
    """ Render the landing page """
    return render(request, 'base.html')


# Class-based view for listing multiple books
class BookListView(LoginRequiredMixin, ListView):

    model = Book
    template_name = 'scroll_core/book_list.html'
    context_object_name = 'books'
    paginate_by = 8

    def get_context_data(self, **kwargs):
        """
        Enhance the base context data with the 'recent_books'
        key that includes recent activity.
        This activity tracks updates and additions of books
        within the last 7 days. It fetches the top 10 most recently
        updated books for the current logged-in user.
        """
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm()
        recent_activity_timeframe = timezone.now() - timezone.timedelta(days=7)
        context['recent_books'] = Book.objects.filter(
            user=self.request.user,
            updated_at__gte=recent_activity_timeframe
        ).order_by('-updated_at')[:10]
        return context

    def get_queryset(self):
        """
        Retrieve a queryset of books based on the presence of a 'query' parameter 
        in the GET request.
        If the 'query' parameter exists, filter books by the title that contains 
        this query, constrained to books owned by the current user. 
        If the 'query' parameter does not exist,return all books owned by the user.
        Returns: A Django QuerySet of Book instances that matches the search criteria
        or all books owned by the user if no search criteria are provided.
        """
        query = self.request.GET.get('query')
        if query:
            return Book.objects.filter(
                Q(title__icontains=query) |
                Q(book_authors__author__last_name__icontains=query),
                user=self.request.user
            ).distinct()
        return Book.objects.filter(
            user=self.request.user
        )


# Class-based view for listing single book
class BookDetailView(DetailView):

    model = Book
    template_name = 'scroll_core/book_detail.html'
    context_object_name = 'book'


    def get_queryset(self):
        """
        Ensure only the owner of the book can access its details.
        """
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset.filter(user=self.request.user)
        else:
            raise Http404("You don't have permisssion to view this book")


    def get_object(self, queryset=None):
        """
        Override get_object to handle a case where a book doesn't belong to the user.
        """
        obj =  super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("You don't have permisssion to view this book")
        return obj



#  A view for creating a new book.
class BookCreateView(LoginRequiredMixin, CreateView):
    """
    A view for creating a new book. Requires users to be authenticated.
    Uses a form generated from the specified fields of the Book model.
    After successfully creating a book, redirects to the book list.
    """

    model = Book
    form_class = BookForm
    template_name = 'scroll_core/book_form.html'

    def form_valid(self, form):
        """
        This will be called when the form is valid and
        assign the current user as the book owner.
        """
        form.instance.user = self.request.user
        response = super(BookCreateView, self).form_valid(form)
        # Set the success message.
        messages.success(self.request, "Book added successfully!")
        return response

    def get_success_url(self):
        """
        Redirect to the book's detail page.
        """
        return reverse_lazy('book-detail', kwargs={'pk': self.object.pk})


# A view for updating a book.
class BookUpdateView(LoginRequiredMixin, UpdateView):
    """
    A view for updating an existing book. Requires users to be authenticated.
    Uses a form generated from the specified fields of the Book model.
    After successfully updating a book, redirects to the book list.
    """
    model = Book
    form_class = BookForm
    template_name = 'scroll_core/book_form.html'

    def get_queryset(self):
        """
        This method ensures that only the books owned by
        the logged-in user can be updated.
        """
        return self.request.user.books.all()
    
    def get_object(self, queryset=None):
        """
        Override get_object to handle a case where a book doesn't belong to the user.
        """
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("You don't have permission to edit this book.")
        return obj

    def form_valid(self, form):
        """
        This will be called when the form is valid and restricts
        updates to user-owned books
        """
        # Set the success message.
        messages.success(self.request, "Book updated successfully!")
        # ensure the form is processed correctly with any additional
        # functionality provided by the parent class.
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the book's detail page.
        """
        return reverse_lazy('book-detail', kwargs={'pk': self.object.pk})


# A view for deleting a book.
class BookDeleteView(LoginRequiredMixin, DeleteView):
    """
    A view for deleting a book. Requires users to be authenticated.
    Confirms book deletion with the user before removing the book
    from the database. After successfully deleting a book, redirects
    to the book list.
    """
    model = Book
    template_name = 'scroll_core/book_confirm_delete.html'
    success_url = reverse_lazy('book-list')

    def get_queryset(self):
        """
        This method ensures that only the books owned by
        the logged-in user can be deleted.
        """
        return self.request.user.books.all()
    
    def get_object(self, queryset=None):
        """
        Override get_object to handle a case where a book doesn't belong to the user.
        """
        obj = super().get_object(queryset=queryset)
        if obj.user != self.request.user:
            raise Http404("You don't have permission to delete this book.")
        return obj

    def delete(self, request, *args, **kwargs):
        """
        This method is called when a DELETE request is received.
        Here we can add additional actions after the book is deleted.
        """
        # Set the success message.
        messages.success(request, "Book deleted successfully!")
        # Continue with the deletion process.S
        return super(
            BookDeleteView, self).delete(request, *args, **kwargs)


logger = logging.getLogger(__name__)
class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    """
    Extends PasswordResetFromKeyView to add 'uidb36' and 'token'
    to the context, ensuring they are available in the template.
    """    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uidb36'] = self.kwargs.get('uidb36')
        context['token'] = self.kwargs.get('key')
        return context
    
    def form_valid(self, form):
        """
        Handles form validation and password reset success.
        """
        response = super().form_valid(form)
        messages.success(self.request, "Password changed successfully!")
        return redirect('account_reset_password_done')
    
    def form_invalid(self, form):
        """
        Handles form validation failure.
        """
        messages.error(self.request, "Password reset failed. Please try again")
        return super().form_invalid(form)




# Error page helpers
def get_redirect_url(request):
    if request.user.is_authenticated:
        return 'book-list'
    return 'home'


# Custom Error pages
def custom_403(request, exception):
    """Custom view to handle 403 Forbidden errors"""
    context = {
        'redirect_url': get_redirect_url(request)
    }
    return render(request, 'errors/403.html', context, status=403)


def custom_404(request, exception):
    """Custom view to handle 404 Not Found errors."""
    context = {
        'redirect_url': get_redirect_url(request)
    }
    return render(request, 'errors/404.html', context, status=404)


def custom_500(request):
    """Custom view to handle 500 Internal Server errors."""
    context = {
        'redirect_url': get_redirect_url(request)
    }
    return render(request, 'errors/500.html', context, status=500)


# Help/Guide page
def guide(request):
    return render(request, 'scroll_core/guide.html')
