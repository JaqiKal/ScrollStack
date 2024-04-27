# scroll_core/views.py

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


# Class-based view for listing multiple books
class BookListView(ListView):

    template_name = 'scroll_core/book_list.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 8

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


# Simple function-based view for the index page
def index(request):
    """ Render the landing page """
    return render(request, 'base.html')

#  A view for creating a new book.
class BookCreateView(LoginRequiredMixin, CreateView):
    """
    A view for creating a new book. Requires users to be authenticated.
    Uses a form generated from the specified fields of the Book model.
    After successfully creating a book, redirects to the book list.
    """

    template_name = 'scroll_core/book_form.html'
    model = Book
    #  success_url = '/book-list/'
    success_url = reverse_lazy('book-list')
    form_class = BookForm

    def form_valid(self, form):
        # Assign the current user as the book owner
        form.instance.user = self.request.user
        response = super(BookCreateView, self).form_valid(form)
        messages.success(self.request, "Book added successfully!")
        return response

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
    success_url = reverse_lazy('book-list')

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
        # Ensure users can only delete their books
        return self.request.user.books.all()
