# Generated by Django 4.1.4 on 2023-07-01 07:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0007_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='unique_identifier',
            new_name='postid',
        ),
    ]
