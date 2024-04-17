from django.conf import settings
from django.db import models
from django.utils.text import slugify


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