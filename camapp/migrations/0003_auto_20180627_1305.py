# Generated by Django 2.0.6 on 2018-06-27 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camapp', '0002_auto_20180627_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fraud',
            name='date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='tableattendance',
            name='date',
            field=models.DateField(default=None),
        ),
    ]
