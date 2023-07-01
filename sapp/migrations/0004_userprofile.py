# Generated by Django 4.1.4 on 2023-07-01 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sapp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(max_length=10)),
                ('bio', models.TextField()),
                ('website', models.URLField()),
                ('location', models.CharField(max_length=100)),
                ('Nationality', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sapp.users')),
            ],
        ),
    ]
