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
    template_name = 'scroll_core/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        """
        This method is overridden to filter the books
        by the logged-in user
        """
        return Book.objects.filter(user=self.request.user)


# Simple function-based view for the index page
def index(request):
    """ Render the landing page """
    return render(request, 'base.html')