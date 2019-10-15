# Generated by Django 2.2.6 on 2019-10-13 06:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contests', '0010_auto_20191013_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contest',
            name='ending_time',
            field=models.DateTimeField(default=datetime.datetime(2019, 10, 20, 6, 52, 0, 829690, tzinfo=utc), help_text='Enter a contest ending time'),
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('finishing_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('contest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contests.Contest')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
