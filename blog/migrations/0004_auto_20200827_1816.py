# Generated by Django 2.2.13 on 2020-08-27 17:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200827_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2020, 8, 27, 17, 16, 39, 896538, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.CharField(choices=[('Achievements', 'Achievements'), ('Education', 'Education'), ('Work Experience', 'Work Experience')], default='Education', max_length=200),
        ),
    ]
