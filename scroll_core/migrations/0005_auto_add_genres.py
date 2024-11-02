# Generated by Django 5.0.4 on 2024-10-30 08:03
# root/scroll_core/migrations/0005_auto_add_genres.py
from django.db import migrations


def add_default_genres(apps, schema_editor):
    Genre = apps.get_model("scroll_core", "Genre")
    default_genres = [
        {
            "name": "Fiction",
            "description": "A genre of speculative narrative fiction."},
        {
            "name": "Non-Fiction",
            "description": "Works based on factual information."
         },
        {
            "name": "Young Adult",
            "description": "Books targeted at young adults."
        },
        {
            "name": "Children's",
            "description": "Books targeted at children."
        },
        {
            "name": "Fantasy",
            "description": "Genre of magical and mythical worlds."
        },
        {
            "name": "Horror",
            "description": "Books designed to elicit fear or suspense."
        },
        {
            "name": "Historical",
            "description": "Books based on historical events."
        },
    ]
    for genre_data in default_genres:
        Genre.objects.create(**genre_data)


class Migration(migrations.Migration):

    dependencies = [
        ('scroll_core', '0004_alter_author_first_name_alter_author_last_name_and_more'),
    ]

    operations = [
        migrations.RunPython(add_default_genres),
    ]