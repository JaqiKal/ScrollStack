# scroll_core/forms.py

from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Book

class BookForm(forms.ModelForm):
    """
    A form for creating or updating a book.
    """
    class Meta:
        model = Book
        fields = ['title', 'genre', 'publication_year', 'isbn', 'description', 'image', 'image_alt']
        widgets = {
            'description': RichTextWidget(attrs={"rows": 5}),
            'image_alt': forms.TextInput(attrs={"placeholder": "Describe the image here"}),
        }
        labels = {
            'title': 'Book Title',
            'genre': 'Genre',
            'isbn': 'ISBN Number',
            'publication_year': 'Publication Year',
            'description': 'Description',
            'image': 'Book Cover Image',
            'image_alt': 'Image Alt Text',
        }
