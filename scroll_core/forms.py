# scroll_core/forms.py

from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Book, Author

class BookForm(forms.ModelForm):
    # Explicitly define author fields if not inheriting directly from an Author model
    author_first_name = forms.CharField(
        max_length=100, 
        required=False, 
        help_text="Enter the author's first name"  # Help text directly defined here
    )
    author_middle_name = forms.CharField(
        max_length=100, 
        required=False, 
        help_text="Optional: enter the author's middle name or initial"  # Help text directly defined here
    )
    author_last_name = forms.CharField(
        max_length=100, 
        required=False, 
        help_text="Enter the author's last name"  # Help text directly defined here
    )

    class Meta:
        model = Book
        fields = [
            'title', 'author_first_name', 'author_middle_name', 'author_last_name', 
            'genre', 'publication_year', 'isbn', 'description', 'image'
        ]
        widgets = {
            'description': RichTextWidget(attrs={"rows": 5}),
        }
        labels = {
            'title': 'Book Title',
            'genre': 'Genre',
            'isbn': 'ISBN Number',
            'publication_year': 'Publication Year',
            'description': 'Description',
            'image': 'Book Cover Image',
        }

