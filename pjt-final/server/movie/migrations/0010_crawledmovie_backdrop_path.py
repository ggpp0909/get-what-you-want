# Generated by Django 3.2.9 on 2021-11-24 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0009_alter_crawledmovie_movie_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawledmovie',
            name='backdrop_path',
            field=models.TextField(null=True),
        ),
    ]