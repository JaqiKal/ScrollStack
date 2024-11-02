# scroll_core/forms.py
# Inspired by various sources, please see README
# Credits & Acknowledgement/Content

from django import forms
from djrichtextfield.widgets import RichTextWidget
from .models import Book, Author, BookAuthor, Genre
from django.core.exceptions import ValidationError
import os


# Author Form
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'middle_name', 'last_name']
        labels = {
            'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name'
        }

    def clean(self):
        cleaned_data = super().clean()
        cleaned_data['first_name'] = cleaned_data.get('first_name', '').strip()
        cleaned_data['middle_name'] = cleaned_data.get('middle_name', '').strip()
        cleaned_data['last_name'] = cleaned_data.get('last_name', '').strip()
        return cleaned_data


# Utility Function: Validate Image File Extension
def validate_image_file_extension(image):
    ext = os.path.splitext(image.name)[1]  # Get the file extension
    valid_extensions = ['.jpg', '.jpeg', '.png', '.webp']
    if ext.lower() not in valid_extensions:
        raise ValidationError(
            'Unsupported file extension.',
            'Only jpg, jpeg, png, and webp are allowed.'
        )


# Book Form
class BookForm(forms.ModelForm):
    author_first_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Enter the author's first name",
            'title': "Please enter the author's first name"
        })
    )
    author_middle_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Optional: enter the author's middle name or initial",
            'title': "Optional: Please enter the author's middle name or initial"
        })
    )
    author_last_name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "Enter the author's last name",
            'title': "Please enter the author's last name"
        })
    )

    class Meta:
        model = Book
        fields = [
            'title', 'author_first_name', 'author_middle_name',
            'author_last_name', 'genre', 'publication_year', 'isbn',
            'description', 'image'
        ]
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title of the book',
                'title': "Please enter the title of the book"
            }),
            'genre': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Select a genre',
                'title': "Please select a genre from the list"
            }),
            'publication_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the publication year',
                'title': "Please enter the publication year"
            }),
            'isbn': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter the ISBN number of the book 10 or 13 digits and a hyphen (format: nnnnnnnnnn/nnn-n)",
                'title': "Please enter the ISBN no."
            }),
            # TODO: Add a custom widget for the description field
            'description': RichTextWidget(attrs={
                'rows': 5,
                'class': 'form-control',
                'placeholder': 'Enter a brief description of the book',
                'title': "Please enter a brief description of the book"
            })
        }
        labels = {
            'title': 'Book Title',
            'genre': 'Select genre',
            'isbn': 'ISBN Number',
            'publication_year': 'Publication Year',
            'description': 'Description',
            'image': 'Upload New Book Cover'
        }

    # TODO: Add a custom clean method for the Image field
    image = forms.ImageField(
        validators=[validate_image_file_extension],
        required=False,
        help_text=(
            "Upload a cover image. Only jpg, jpeg, png, "
            "and webp formats are allowed."
        )
    )

    def clean(self):
        """
        Override the clean method to strip leading/trailing spaces
        from the book title, author fields, and description.
        """
        cleaned_data = super().clean()
        cleaned_data['title'] = cleaned_data.get('title', '').strip()
        cleaned_data['author_first_name'] = cleaned_data.get(
            'author_first_name', ''
        ).strip()
        cleaned_data['author_middle_name'] = cleaned_data.get(
            'author_middle_name', ''
        ).strip()
        cleaned_data['author_last_name'] = cleaned_data.get(
            'author_last_name', ''
        ).strip()
        cleaned_data['description'] = cleaned_data.get(
            'description', ''
        ).strip()
        return cleaned_data

    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn', '').strip()
        # Remove hyphens from ISBN for validation
        isbn_digits = isbn.replace('-', '')

        # Check if the ISBN digits are only numeric and 10 or 13 digits long
        if not isbn_digits.isdigit() or len(isbn_digits) not in [10, 13]:
            raise forms.ValidationError(
                "Enter a valid ISBN number. ISBN should be 10 or 13 digits "
                "long including a hyphen (xxx-...)."
            )
        return isbn  # Return the original ISBN with hyphens

    def __init__(self, *args, **kwargs):
        """
        Initialize the form; if editing an existing book,
        set initial values for author fields.
        """
        super(BookForm, self).__init__(*args, **kwargs)
        if self.instance.pk:
            authors = self.instance.get_authors()
            if authors:
                author = authors[0]  # Assuming only one author for simplicity
                self.fields['author_first_name'].initial = author.first_name
                self.fields['author_middle_name'].initial = author.middle_name
                self.fields['author_last_name'].initial = author.last_name
                self.initial['author_id'] = author.id

    def save(self, commit=True):
        """
        Save the form instance and handle the creation or linking
        of the author. Avoid duplicate author entries and ensure author
        details are updated if necessary.
        """
        book = super(BookForm, self).save(commit=False)

        # Handle author creation, remove any leading or trailing whitespace
        first_name = self.cleaned_data.get('author_first_name', '').strip()
        middle_name = self.cleaned_data.get('author_middle_name', '').strip()
        last_name = self.cleaned_data.get('author_last_name', '').strip()

        if first_name and last_name:
            # Find existing author or create a new one
            author, created = Author.objects.update_or_create(
                id=self.initial.get('author_id'),
                defaults={
                    'first_name': first_name,
                    'middle_name': middle_name if middle_name else None,
                    'last_name': last_name
                }
            )

            # Ensure the book is saved before trying to link it
            if commit:
                book.save()
                self.save_m2m()  # Save many-to-many fields

            # Check if book-author link already exists to avoid duplicate link
            if not BookAuthor.objects.filter(
                book=book, author=author
            ).exists():
                BookAuthor.objects.create(book=book, author=author)

        else:
            if commit:
                book.save()
                self.save_m2m()

        # Remove the book cover image if the checkbox is checked
        if self.cleaned_data.get('remove_image', False):
            book.remove_image()

        return book


# Book Search Form
class BookSearchForm(forms.Form):
    """
    A form field for searching books by title & author
    """
    query = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Search by title or author last-name'
            }
        )
    )

    def clean_query(self):
        """
        Ensure the search query is not empty and strip extra spaces.
        """
        query = self.cleaned_data['query'].strip()
        if not query:
            raise forms.ValidationError("Search field cannot be empty.")
        return query

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label='Name',  # Custom label
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'}))
    email = forms.EmailField(
        required=True,
        label='e-mail',  # Custom label
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your e-mail address'}))
    subject = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter the subject'}))
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'form-control', 'rows': 5,
            'placeholder': 'Enter your message'}))