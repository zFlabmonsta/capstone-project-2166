# Generated by Django 2.2.2 on 2019-07-24 17:11

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190724_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='display_image',
            field=models.ImageField(blank=True, null=True, upload_to=main.models.image_directory_path),
        ),
    ]