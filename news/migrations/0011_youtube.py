# Generated by Django 2.2 on 2020-08-13 14:21

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0010_auto_20200813_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yt_vid', embed_video.fields.EmbedVideoField(blank=True, max_length=140)),
            ],
        ),
    ]
