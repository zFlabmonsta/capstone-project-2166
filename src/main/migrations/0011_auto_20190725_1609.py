# Generated by Django 2.2.2 on 2019-07-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20190725_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='elevator',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='ramp',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='travelator',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]