# scroll_manager/urls.py

"""
URL configuration for scroll_manager project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler403, handler404, handler500
from scroll_core.views import custom_403, custom_404, custom_500

urlpatterns = [

    # Admin site URLs, provides a web-based interface
    # for managing the site.
    path('admin/', admin.site.urls),

    # Include app URLs
    path('', include('scroll_core.urls')),
    path('home/', include('scroll_home.urls')),
    path('accounts/', include('allauth.urls')),
    path('djrichtextfield/', include('djrichtextfield.urls')),
   
]

# Setting custom error handlers
handler403 = 'scroll_core.views.custom_403'
handler404 = 'scroll_core.views.custom_404'
handler500 = 'scroll_core.views.custom_500'