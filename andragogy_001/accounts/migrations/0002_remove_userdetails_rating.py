# Generated by Django 4.2.7 on 2024-01-25 21:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetails',
            name='rating',
        ),
    ]
