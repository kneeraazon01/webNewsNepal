# Generated by Django 2.2 on 2020-08-16 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0015_newsletter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='user_id',
        ),
    ]