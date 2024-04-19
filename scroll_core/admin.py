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


# Define a function to unregister models safely
def unregister_if_registered(model):
    try:
        admin.site.unregister(model)
    except admin.sites.NotRegistered:
        pass


# Unregister previously registered models without customization
unregister_if_registered(Book)
unregister_if_registered(Author)
unregister_if_registered(Genre)
unregister_if_registered(BookAuthor)

# Re-register models with custom admin configurations
admin.site.register(Genre, GenreAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookAuthor)  # No admin customization is needed here
