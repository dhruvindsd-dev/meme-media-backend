# Generated by Django 3.1.2 on 2020-10-14 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('memes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Memes',
            new_name='Meme',
        ),
    ]