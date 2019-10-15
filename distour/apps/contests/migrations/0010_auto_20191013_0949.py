# Generated by Django 2.2.6 on 2019-10-13 06:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0009_auto_20191013_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='ending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 6, 49, 17, 482370, tzinfo=utc), help_text='Enter a contest ending time'),
        ),
    ]
