# Generated by Django 2.2.13 on 2020-08-29 13:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200828_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 29, 13, 53, 26, 770697, tzinfo=utc)),
        ),
    ]
