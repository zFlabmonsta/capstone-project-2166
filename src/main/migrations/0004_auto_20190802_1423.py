# Generated by Django 2.2.2 on 2019-08-02 14:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190802_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
