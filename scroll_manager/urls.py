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
from scroll_core import views as index_views
from scroll_core.views import dashboard


urlpatterns = [

    # Admin site URLs, provides a web-based interface
    # for managing the site.
    path('admin/', admin.site.urls),

    # Include scroll_core URLs
    path('', include('scroll_core.urls')),

    # Authentication URLs, incl URLs provided by
    # django-allauth for user authentication.
    path('accounts/', include('allauth.urls')),

    # Dashboard URL, uses a function view from the
    # scroll_core app to display the dashboard.
    path('dashboard/', dashboard, name='dashboard'),

]
