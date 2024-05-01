# scroll_core/views.py
from django.shortcuts import render
from django.http import (
    HttpResponse, HttpResponseRedirect, HttpResponseForbidden,
    HttpResponseNotFound, HttpResponseServerError
)
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.utils import timezone
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Profile




# Simple function-based view for the index page
def index(request):
    """ Render the landing page """
    return render(request, 'base.html')


# Class-based view for listing multiple books
class BookListView(ListView):

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
        recent_activity_timeframe = timezone.now() - timezone.timedelta(days=7)
        context['recent_books'] = Book.objects.filter(
            user=self.request.user,
            updated_at__gte=recent_activity_timeframe
        ).order_by('-updated_at')[:10]
        return context

    def get_queryset(self):
        """
        This method is overridden to filter the books
        by the logged-in user
        """
        return Book.objects.filter(user=self.request.user)


# Class-based view for listing single book
class BookDetailView(DetailView):

    model = Book
    template_name = 'scroll_core/book_detail.html'
    context_object_name = 'book'


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

    def delete(self, request, *args, **kwargs):
        """
        This method is called when a DELETE request is received.
        Here we can add additional actions after the book is deleted.
        """
        # Set the success message.
        messages.success(request, "Book deleted successfully!")
        # Continue with the deletion process.
        return super(
            BookDeleteView, self).delete(request, *args, **kwargs)


# Profile view
@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'scroll_core/profile.html', {'profile': user_profile})


# Error pages
def custom_403(request, exception):
    """Custom view to handle 403 Forbidden errors."""
    return HttpResponseForbidden(render(request, 'errors/403.html'))


def custom_404(request, exception):
    """Custom view to handle 404 Not Found errors."""
    return HttpResponseNotFound(render(request, 'errors/404.html'))


def custom_500(request):
    """Custom view to handle 500 Internal Server errors."""
    return HttpResponseServerError(render(request, 'errors/500.html'))
