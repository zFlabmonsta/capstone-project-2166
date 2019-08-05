# Generated by Django 2.2.2 on 2019-08-04 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_booking_reviewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='property',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='property',
            name='house',
        ),
        migrations.RemoveField(
            model_name='property',
            name='resort',
        ),
        migrations.RemoveField(
            model_name='property',
            name='townhouse',
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
