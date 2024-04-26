# scroll_core/views.py

from django.shortcuts import render
from django.http import HttpResponse
# Import the ListView
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# The Book model is imported
from .models import Book
# Importing LoginRequiredMixin to ensure that only authenticated 
# users can access specific views.
from django.contrib.auth.mixins import LoginRequiredMixin


# Class-based view for listing books
class BookListView(ListView):
    model = Book
    template_name = 'scroll_core/book_list.html'
    context_object_name = 'books'
    paginate_by = 4

    def get_queryset(self):
        """
        This method is overridden to filter the books
        by the logged-in user
        """
        return Book.objects.filter(user=self.request.user)

class BookDetailView(DetailView):
    model = Book
    template_name = 'scroll_core/book_detail.html'
    context_object_name = 'book'

# Simple function-based view for the index page
def index(request):
    """ Render the landing page """
    return render(request, 'base.html')

class BookCreateView(LoginRequiredMixin, CreateView):
    """
    A view for creating a new book. Requires users to be authenticated.
    Uses a form generated from the specified fields of the Book model.
    After successfully creating a book, redirects to the book list.
    """
    model = Book
    fields = ['title', 'genre', 'publication_year', 'isbn', 'description', 'image']
    template_name = 'scroll_core/book_form.html'
    success_url = '/book-list/'

class BookUpdateView(LoginRequiredMixin, UpdateView):
    """
    A view for updating an existing book. Requires users to be authenticated.
    Uses a form generated from the specified fields of the Book model.
    After successfully updating a book, redirects to the book list.
    """
    model = Book
    fields = ['title', 'genre', 'publication_year', 'isbn', 'description', 'image']
    template_name = 'scroll_core/book_form.html'
    success_url = '/book-list/'

class BookDeleteView(LoginRequiredMixin, DeleteView):
    """
    A view for deleting a book. Requires users to be authenticated.
    Confirms book deletion with the user before removing the book from the database.
    After successfully deleting a book, redirects to the book list.
    """
    model = Book
    template_name = 'scroll_core/book_confirm_delete.html'
    success_url = '/book-list/'