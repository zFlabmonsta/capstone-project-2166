# Generated by Django 2.2.2 on 2019-07-12 08:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190712_0756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]