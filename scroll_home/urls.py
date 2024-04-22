# scroll_home/urls.py

from django.urls import path
from .views import Index

urlpatterns = [
    path('', Index.as_view(), name='home'),  # Root URL of the site
]
