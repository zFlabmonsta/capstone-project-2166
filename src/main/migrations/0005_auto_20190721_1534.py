# Generated by Django 2.2.2 on 2019-07-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190721_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.CharField(blank=True, max_length=10000000000, null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='time_booked',
            field=models.IntegerField(default=0),
        ),
    ]
