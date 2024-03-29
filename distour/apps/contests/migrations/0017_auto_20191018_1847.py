# Generated by Django 2.2.6 on 2019-10-18 15:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0016_auto_20191018_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='point',
            name='last_checked',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='contest',
            name='ending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 25, 15, 47, 43, 862006, tzinfo=utc), help_text='Enter a contest ending time'),
        ),
    ]
