# scroll_core/urls.py

from django.urls import path, include
from .views import index, BookListView

urlpatterns = [

    path('books/', BookListView.as_view(), name='book-list'),
    path('djrichtextfield/', include('djrichtextfield.urls')),
    path('', index, name='index'),

]
