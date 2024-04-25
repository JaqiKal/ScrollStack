# Generated by Django 5.0.4 on 2024-04-25 13:55

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scroll_core', '0009_alter_book_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, default='static/images/default-book-200.webp', force_format='WEBP', keep_meta=True, null=True, quality=75, scale=None, size=[400, None], upload_to='scroll_core/'),
        ),
        migrations.AddField(
            model_name='book',
            name='image_alt',
            field=models.CharField(default='Book cover', max_length=255),
        ),
    ]
