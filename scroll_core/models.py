from django.conf import settings
from django.db import models
from django.utils.text import slugify
# Amended: https://www.geeksforgeeks.org/how-to-use-regex-validator-in-django/
from django.core.validators import RegexValidator


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
        blank=True,  # Makes the field optional
        null=True
    )
    last_name = models.CharField(
        max_length=100,
        validators=[name_validator],
        verbose_name="Last Name",
        help_text="Enter the author's last name"
    )

    def __str__(self):
        # Constructs a full name with components that are present
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
        help_text="Enter a URL-friendly name"
    )
    publication_year = models.IntegerField(
        verbose_name="Publication Year",
        help_text="Enter the year the book was published"
    )
    isbn = models.CharField(
        max_length=13, unique=True,
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
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            # Generate slug from book title if not provided
            self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

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

