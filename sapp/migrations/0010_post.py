# Generated by Django 4.1.4 on 2023-07-01 07:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0009_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('caption', models.TextField()),
                ('image_or_video_content', models.ImageField(upload_to='post_content/')),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
