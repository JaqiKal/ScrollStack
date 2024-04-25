from django.conf import settings
from django.db import models
from django.utils.text import slugify
# Amended: Incorporating RegexValidator for input validation as demonstrated
# in the provided reference:
# https://www.geeksforgeeks.org/how-to-use-regex-validator-in-django/
from django.core.validators import RegexValidator
from djrichtextfield.models import RichTextField
from django_resized  import ResizedImageField

class Genre(models.Model):
    """
    Model representing a genre category. Each genre has a name and
    a description which describes what the genre encompasses.

    'verbose_name' - Django Built-in Field Validation, amended from
    https://www.geeksforgeeks.org/verbose_name-django-built-in-field-validation/
    Present in all the models where applicable.
    """
    name = models.CharField(
        max_length=100,
        verbose_name="Genre Name",
        help_text="Enter the name of the genre"
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Enter a description for this genre"
    )

    # Returns the name of the genre when the object is printed,
    # enhancing readability in admin panels.
    def __str__(self):
        return self.name


class Author(models.Model):
    """
    Model representing an author. Authors have first, middle (optional),
    and last names. Each author could potentially write multiple books.

    'verbose_name' - Django Built-in Field Validation, amended from
    https://www.geeksforgeeks.org/verbose_name-django-built-in-field-validation/
    """
    # Validator for names, allowing only alphabetic characters
    # and basic punctuation
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z,.\s-]+$',
        message="""Names must contain only letters,
        spaces, commas, periods, or hyphens."""
    )

    first_name = models.CharField(
        max_length=100,
        validators=[name_validator],
        verbose_name="First Name",
        help_text="Enter the author's first name"
    )
    middle_name = models.CharField(
        max_length=100,
        validators=[name_validator],
        verbose_name="Middle Name",
        help_text="Enter the author's middle name or initial",
        blank=True,  # Optional field.
        null=True  # Allows storing null in the database for middle name.
    )
    last_name = models.CharField(
        max_length=100,
        validators=[name_validator],
        verbose_name="Last Name",
        help_text="Enter the author's last name"
    )

    def get_books(self):
        """
        This method returns a list of Book objects associated with this author.
        """
        return [book_author.book for book_author in self.book_authors.all()]

    def __str__(self):
        # Construct full name by concatenating first,
        # middle (if exists), & last names.
        full_name = f"{self.first_name}"
        if self.middle_name:
            full_name += f" {self.middle_name}"
        full_name += f" {self.last_name}"
        return full_name.strip()


class Book(models.Model):
    """
    Model representing a book. Each book has a title, publication year, ISBN,
    and is linked to a genre and an owner (user). Slugs are used to create
    friendly URL paths.
    Inspired by Dee Mc videos, se README for credit.

    'verbose_name' - Django Built-in Field Validation, amended from
    https://www.geeksforgeeks.org/verbose_name-django-built-in-field-validation/
    """
    title = models.CharField(
        max_length=255,
        verbose_name="Book Title",
        help_text="Enter the title of the book"
    )
    slug = models.SlugField(
        unique=True, blank=True,
        help_text="A URL-friendly name is entered automatically on save"
    )
    publication_year = models.IntegerField(
        verbose_name="Publication Year",
        help_text="Enter the year the book was published"
    )

    # Validator for ISBN to ensure format correctness.
    isbn_validator = RegexValidator(
        regex=r'^[\d-]+$',
        message="ISBN must only contain numbers and hyphens."
    )
    isbn = models.CharField(
        max_length=17, unique=True,
        validators=[isbn_validator],
        verbose_name="ISBN",
        help_text="Enter the ISBN number of the book"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='books',
        help_text="Select the owner of the book"
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE,
        related_name='books',
        help_text="Select the genre of the book"
    )
    added_at = models.DateField(
        auto_now_add=True,
        verbose_name="Date Added",
        null=True
    )
    description = RichTextField(
        verbose_name="Description",
        help_text="Enter a brief description of the book",
        blank=True  # Optional: make this field not required
    )
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="scroll_core/",
        force_format="WEBP",
        blank=False,
        null=True,
        default='static/images/default-book-200.webp'
    )
    image_alt = models.CharField(
        max_length=255, 
        null=False, 
        blank=False,
        default='Book cover'
    )
   
    def save(self, *args, **kwargs):
        if not self.slug:
            # Automatically generate slug from book title if not provided
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)


    def get_authors(self):
        """
        This method returns a list of Author objects associated with this book.
        """
        return [book_author.author for book_author in self.book_authors.all()]

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    """
    Model representing the many-to-many relationship between Books and Authors.
    This is a bridge table that allows for the association of multiple authors
    with a single book and vice versa.
    """
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        related_name='book_authors',
        help_text="Select the book associated with an author"
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE,
        related_name='book_authors',
        help_text="Select the author associated with a book"
    )
