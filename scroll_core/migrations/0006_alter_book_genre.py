# Generated by Django 5.0.4 on 2024-10-30 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scroll_core', '0005_auto_add_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to='scroll_core.genre'),
        ),
    ]
