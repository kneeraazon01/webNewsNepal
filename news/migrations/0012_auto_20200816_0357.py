# Generated by Django 2.2 on 2020-08-16 03:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_youtube'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='photo_0',
            new_name='photo',
        ),
    ]
