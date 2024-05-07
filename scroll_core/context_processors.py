# Amended from https://djangocentral.com/how-to-create-custom-context-processors-in-django/

from .models import Book

def user_book_statistics(request):
    """
    Add book statistics.
    """
    if request.user.is_authenticated:
        book_count = Book.objects.filter(user=request.user).count()
    else:
        book_count = 0

    return { 
        'user_book_count': book_count,
    }