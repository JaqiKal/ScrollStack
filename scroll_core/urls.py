# scroll_core/urls.py

from django.urls import path, include
from .views import index, BookListView, BookDetailView

urlpatterns = [

    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', index, name='index'),

]
