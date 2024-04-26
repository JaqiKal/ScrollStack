# scroll_core/views.py

from django.shortcuts import render
from django.http import HttpResponse
# Import the ListView
from django.views.generic import ListView
# The Book model is imported
from .models import Book


# Class-based view for listing books
class BookListView(ListView):
    model = Book
    template_name = 'dashboard/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        """
        This method is overridden to filter the books
        by the logged-in user
        """
        return Book.objects.filter(user=self.request.user)

# Create your views here


def index(request):
    """ Render the landing page """
    return render(request, 'base.html')


def dashboard(request):
    """ Fetch the books associated with the logged-in user"""
    user_books = Book.objects.filter(
        user=request.user
    ).prefetch_related('book_authors__author')
    return render(request, 'dashboard/main.html', {'books': user_books})
