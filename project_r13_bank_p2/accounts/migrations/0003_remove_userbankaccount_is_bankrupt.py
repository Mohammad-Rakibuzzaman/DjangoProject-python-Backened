# Generated by Django 4.2.7 on 2024-01-17 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userbankaccount_is_bankrupt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbankaccount',
            name='is_bankrupt',
        ),
    ]
