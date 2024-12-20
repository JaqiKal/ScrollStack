from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.core.validators import (
    RegexValidator,
    MaxValueValidator,
    MinValueValidator
)
from djrichtextfield.models import RichTextField
from cloudinary.models import CloudinaryField
from datetime import datetime
from django.contrib.auth.models import User


class Genre(models.Model):
    """
    Model representing a genre category. Each genre has a name and
    a description which describes what the genre encompasses.
    """
    name = models.CharField(
        max_length=100,
        verbose_name='Genre Name',
    )
    description = models.TextField(
        verbose_name='Description',
    )

    def __str__(self):
        return self.name


class Author(models.Model):
    """
    Model representing an author. Authors have first, middle (optional),
    and last names. Each author could potentially write multiple books.
    """
    name_validator = RegexValidator(
        regex=r'^[a-zA-Z,.\s-]+$',
        message=(
            'Names must contain only letters, spaces,'
            'commas, periods, or hyphens.'
        )
    )

    first_name = models.CharField(
        max_length=100,
        validators=[name_validator],
        verbose_name='First Name',
    )
    middle_name = models.CharField(
        max_length=100,
        validators=[name_validator],
        verbose_name='Middle Name',
        blank=True,
        null=True
    )
    last_name = models.CharField(
        max_length=100,
        validators=[name_validator],
        verbose_name='Last Name',
        blank=False  # Not optional
    )

    def __str__(self):
        parts = [self.first_name, self.middle_name, self.last_name]
        full_name = " ".join(part for part in parts if part)
        return full_name or "Unnamed Author"


class Book(models.Model):
    """
    Model representing a book. Each book has a title, publication year, ISBN,
    and is linked to a genre and an owner (user). Slugs are used to create
    friendly URL paths.
    """
    title = models.CharField(
        max_length=255,
        verbose_name='Book Title',
    )
    class Meta:
        ordering = ['title']  # Orders by title alphabetically by default

    slug = models.SlugField(
        max_length=255,
        unique=True, blank=True,
        help_text='A URL-friendly name is entered automatically on save'
    )
    publication_year = models.IntegerField(
        validators=[
            # Ensures the year is not in the future
            MaxValueValidator(datetime.now().year),
            # Ensures the year has at least four digits
            MinValueValidator(1000)
        ],
        verbose_name='Publication Year',
        null=True,
        blank=True
    )
    isbn_validator = RegexValidator(
        regex=r'^[\d-]+$',
        message='ISBN must only contain numbers and hyphens.'
    )
    isbn = models.CharField(
        max_length=14,
        unique=True,
        validators=[isbn_validator],
        verbose_name='ISBN',
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='books',
    )
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE,
        related_name='books',
    )
    added_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date Added',
        null=True
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date Updated',
        null=True
    )
    deleted_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date Deleted',
        null=True
    )
    description = RichTextField(
        verbose_name='Description',
        blank=True
    )
    image = CloudinaryField(
        'image',
        default=(
            'https://res.cloudinary.com/dsbcjtatz/image/upload/v1714578907/'
            'scroll_core/book_cover_images/default-book-cover_t2lyio.webp'
        ),
        folder='scroll_core/book_cover_images',
        transformation={
            'width': 150,
            'height': 225,
            'crop': 'fill',
            'format': 'webp',
            'quality': "auto:good"
        },
        allowed_formats=['webp', 'jpg', 'jpeg', 'png']
    )
    image_alt = models.CharField(
        max_length=255,
        default='Book cover'
    )

    def save(self, *args, **kwargs):
        """Ensure saved slug is unique"""
        if not self.slug:
            self.slug = slugify(self.title)

        queryset = Book.objects.filter(slug=self.slug)
        if self.pk:
            queryset = queryset.exclude(pk=self.pk)

        if queryset.exists():
            base_slug = self.slug
            i = 1
            while queryset.exists():
                self.slug = f"{base_slug}-{i}"
                queryset = Book.objects.filter(slug=self.slug)
                i += 1

        super(Book, self).save(*args, **kwargs)

    def get_authors(self):
        return [book_author.author for book_author in self.book_authors.all()]

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def remove_image(self):
        """
        Removes the current image of the book by setting
        it back to the default value.
        """
        self.image = (
            'https://res.cloudinary.com/dsbcjtatz/image/upload/v1714578907/'
            'scroll_core/book_cover_images/default-book-cover_t2lyio.webp'
        )
        self.save()

    def __str__(self):
        return self.title


class BookAuthor(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE,
        related_name='book_authors'
    )
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE,
        related_name='book_authors'
    )


# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = CloudinaryField(
        'image',
        default=(
            'https://res.cloudinary.com/dsbcjtatz/image/upload/v1714579934/'
            'scroll_core/user_profile_image/default-profile-image_qscipu.webp'
        ),
        # Profile images are stored
        folder='scroll_core/user_profile_images',
        transformation={
            'width': 150,
            'height': 200,
            'crop': 'fill',
            'format': 'webp',
            'quality': "auto:good"
        },
        allowed_formats=['webp', 'jpg', 'jpeg', 'png']
    )
    bio = models.TextField()

    def __str__(self):
        return self.user.username
