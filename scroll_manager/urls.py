# scroll_manager/urls.property

"""
URL configuration for scroll_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler403, handler404, handler500
from django.shortcuts import render 
# from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseServerError
# from django.core.exceptions import PermissionDenied


# Define a simple view that intentionally raises a 404 error
# def test_404(request):
   # raise Http404("Test 404 Page Not Found")

# Define a simple view that intentionally raises a 403 error
# def test_403(request):
  #  raise PermissionDenied("Test 403 Permission Denied")

# Define a simple view that intentionally raises a 500 error
def test_500(request):
    raise Exception("Test 500 Internal Server Error")


urlpatterns = [

    # Admin site URLs, provides a web-based interface
    # for managing the site.
    path('admin/', admin.site.urls),

    # Include scroll_core URLs
    path('', include('scroll_core.urls')),

    # Include scroll_home URLs, handel the root
    path('home/', include('scroll_home.urls')),

    # Authentication URLs, incl URLs provided by
    # django-allauth for user authentication.
    path('accounts/', include('allauth.urls')),

    path('djrichtextfield/', include('djrichtextfield.urls')),

   # path('test-403/', test_403, name='test-403'),
   # path('test-404/', test_404, name='test-404'),
   # path('test-500/', test_500, name='test-500'),

]

# Setting custom error handlers
# handler403 = 'scroll_core.views.custom_403'
# handler404 = 'scroll_core.views.custom_404'
# handler500 = 'scroll_core.views.custom_500'