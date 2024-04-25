# scroll_core/urls.py

from django.urls import path, include
from .views import index, dashboard, BookListView 

urlpatterns = [
   
    path('books/', BookListView.as_view(), name='book-list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', index, name='index'),


]