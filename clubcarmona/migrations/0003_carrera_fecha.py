# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-13 14:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0002_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrera',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 13, 14, 51, 17, 631257, tzinfo=utc)),
        ),
    ]
