# Generated by Django 5.0.4 on 2024-04-28 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scroll_core', '0012_alter_author_last_name_alter_author_middle_name_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(help_text="Enter the author's last name", max_length=100, validators=[django.core.validators.RegexValidator(message='Names must contain only letters,\n        spaces, commas, periods, or hyphens.', regex='^[a-zA-Z,.\\s-]+$')], verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(blank=True, help_text="Optional: Enter the author's middle name or initial", max_length=100, null=True, validators=[django.core.validators.RegexValidator(message='Names must contain only letters,\n        spaces, commas, periods, or hyphens.', regex='^[a-zA-Z,.\\s-]+$')], verbose_name='Middle Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(help_text='Enter the title of the book', max_length=255, verbose_name='Book Title'),
        ),
    ]