# Generated by Django 2.2.2 on 2019-08-04 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_activities'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='url_image',
            new_name='image_url',
        ),
    ]
