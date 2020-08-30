# Generated by Django 2.2.13 on 2020-08-29 19:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200829_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='datetime',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cv',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 19, 31, 21, 202643, tzinfo=utc)),
        ),
    ]
