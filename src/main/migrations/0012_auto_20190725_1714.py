# Generated by Django 2.2.2 on 2019-07-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190725_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='apartment',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='hotel',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='house',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='resort',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='townhouse',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]