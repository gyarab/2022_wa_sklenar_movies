# Generated by Django 4.1.7 on 2023-05-02 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_comment_comment_comment_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='movie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movies'),
        ),
    ]