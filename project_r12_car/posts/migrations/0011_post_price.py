# Generated by Django 4.2.7 on 2024-01-15 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0010_alter_comment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=None),
        ),
    ]
