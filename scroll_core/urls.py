# scroll_core/urls.py

from django.urls import path, include
from .views import (index, BookListView, BookDetailView, BookCreateView,
                    BookUpdateView, BookDeleteView, guide,
                    contact_view)

urlpatterns = [
    path('', index, name='index'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/add/', BookCreateView.as_view(), name='book-create'),
    path(
        'books/<int:pk>/edit/',
        BookUpdateView.as_view(),
        name='book-update'
    ),
    path(
        'books/<int:pk>/delete/',
        BookDeleteView.as_view(),
        name='book-delete'
    ),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('guide/', guide, name='guide'),
    path('contact/', contact_view, name='contact'),
]
