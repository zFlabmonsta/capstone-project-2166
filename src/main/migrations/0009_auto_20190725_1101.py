# Generated by Django 2.2.2 on 2019-07-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190724_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='free_parking',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='gym',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='pool',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='property',
            name='spa',
            field=models.BooleanField(default=False),
        ),
    ]
