from django.contrib import admin
from .models import Genre, Author, Book, BookAuthor, RichTextField
from djrichtextfield.widgets import RichTextWidget
from .models import Profile



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'publication_year',
                    'isbn', 'description', 'image')
    list_filter = ("genre",)
    search_fields = ('title', 'isbn')
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        RichTextField: {'widget': RichTextWidget()},
    }

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'middle_name', 'last_name')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(BookAuthor)  # No admin customization is needed here

admin.site.register(Profile)