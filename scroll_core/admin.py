from django.contrib import admin
from .models import Genre
from .models import Author

# Register your models here.
admin.site.register(Genre)
admin.site.register(Author)