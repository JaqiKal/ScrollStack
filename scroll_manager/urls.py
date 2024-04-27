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
from django.http import HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden
from django.shortcuts import render 


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



]

def custom_404(request, exception):
    return HttpResponseNotFound(render(request, 'errors/404.html', {}, status=404))

def custom_500(request):
    return HttpResponseServerError(render(request, 'errors/500.html', {}, status=500))

def custom_403(request, exception):
    return HttpResponseForbidden(render(request, 'errors/403.html', {}, status=403))

# Linking the custom error handlers
handler403 = custom_403
handler404 = custom_404
handler500 = custom_500