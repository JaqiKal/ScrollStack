# scroll_core/views.py
 
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """ Render the landing page """
    return render(request, 'base.html')


def dashboard(request):
    return render(request, 'dashboard/main.html')
