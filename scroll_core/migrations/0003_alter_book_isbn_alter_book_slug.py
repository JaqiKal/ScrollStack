# Generated by Django 5.0.4 on 2024-05-08 15:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scroll_core', '0002_alter_book_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='Enter the ISBN number of the book 10 or 13 digits and hyphen (format: nnn-n...)', max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='ISBN must only contain numbers and hyphens.', regex='^[\\d-]+$')], verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(blank=True, help_text='A URL-friendly name is entered automatically on save', max_length=255, unique=True),
        ),
    ]