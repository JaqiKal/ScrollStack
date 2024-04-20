from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    """ Render the landing page """
    return render(request, 'index.html')
    # return HttpResponse("Hello World!")


def dashboard(request):
    return render(request, 'dashboard/main.html')
