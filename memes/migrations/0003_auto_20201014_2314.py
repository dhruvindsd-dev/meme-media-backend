# Generated by Django 3.1.2 on 2020-10-14 17:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('memes', '0002_auto_20201014_2313'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
        migrations.RenameModel(
            old_name='Likes',
            new_name='Like',
        ),
    ]