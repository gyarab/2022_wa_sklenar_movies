# Generated by Django 4.1.7 on 2023-05-02 06:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_actor_comment_director_photo_url_director_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movies.movies'),
            preserve_default=False,
        ),
    ]
