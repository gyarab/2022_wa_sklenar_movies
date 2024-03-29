# Generated by Django 4.1.7 on 2023-03-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_director_alter_movies_year_movies_director'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='Director',
            new_name='director',
        ),
        migrations.AddField(
            model_name='movies',
            name='genres',
            field=models.ManyToManyField(to='movies.genres'),
        ),
    ]
