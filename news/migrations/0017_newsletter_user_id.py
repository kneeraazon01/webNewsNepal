# Generated by Django 2.2 on 2020-08-16 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0016_remove_newsletter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsletter',
            name='user_id',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
