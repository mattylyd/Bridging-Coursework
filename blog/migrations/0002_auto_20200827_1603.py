# Generated by Django 2.2.13 on 2020-08-27 15:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 15, 3, 4, 45649, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]