# scroll_core/urls.py

from django.urls import path, include
from .views import index, dashboard, BookListView 

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('books/', BookListView.as_view(), name='book-list'), 
    path('djrichtextfield/', include('djrichtextfield.urls')),

]