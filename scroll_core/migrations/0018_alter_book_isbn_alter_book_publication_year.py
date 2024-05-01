# Generated by Django 5.0.4 on 2024-05-01 02:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scroll_core', '0017_alter_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='Enter the ISBN number of the book', max_length=14, unique=True, validators=[django.core.validators.RegexValidator(message='ISBN must only contain numbers and hyphens.', regex='^[\\d-]+$')], verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(blank=True, help_text='Enter the year the book was published, must be a four-digit year', null=True, validators=[django.core.validators.MaxValueValidator(2024), django.core.validators.MinValueValidator(1000)], verbose_name='Publication Year'),
        ),
    ]
