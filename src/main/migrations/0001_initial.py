# Generated by Django 2.2.2 on 2019-07-05 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dashboard_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=20)),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Dashboard')),
            ],
        ),
        migrations.CreateModel(
            name='learning_outcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('learning_outcome', models.CharField(max_length=1000)),
                ('my_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.MyClass')),
            ],
        ),
    ]