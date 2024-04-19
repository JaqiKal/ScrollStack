from django.contrib import admin
from .models import Genre, Author, Book, BookAuthor


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'publication_year',
                    'isbn', 'description')
    search_fields = ('title', 'isbn')
    prepopulated_fields = {'slug': ('title',)}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Register models with custom admin configurations
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor)  # No admin customization is needed here
