# Generated by Django 4.1.7 on 2023-06-04 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_comment_movie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='comments',
        ),
    ]
