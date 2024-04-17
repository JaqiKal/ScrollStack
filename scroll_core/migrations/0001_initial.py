# Generated by Django 5.0.4 on 2024-04-17 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter the name of the genre', max_length=100, verbose_name='Genre Name')),
                ('description', models.TextField(help_text='Enter a description for this genre', verbose_name='Description')),
            ],
        ),
    ]
