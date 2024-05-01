# scroll_manager/urls.property

"""
URL configuration for scroll_manager project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler403, handler404, handler500
from django.shortcuts import render 
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseServerError
from django.core.exceptions import PermissionDenied
# 2 files below serve media files during development, Testing
from django.conf import settings
from django.conf.urls.static import static


# Test: Define a simple view that intentionally raises a 404 error
# def test_404(request):
   # raise Http404("Test 404 Page Not Found")

# Test: Define a simple view that intentionally raises a 403 error
# def test_403(request):
  #  raise PermissionDenied("Test 403 Permission Denied")

# Test: Define a simple view that intentionally raises a 500 error
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


# Testing and debugging
# add files in the media root folder and django will 
# serve them from the media url
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Setting custom error handlers
handler403 = 'scroll_core.views.custom_403'
handler404 = 'scroll_core.views.custom_404'
handler500 = 'scroll_core.views.custom_500'