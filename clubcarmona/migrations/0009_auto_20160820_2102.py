# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0008_auto_20160820_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 20, 21, 2, 53, 566365)),
        ),
    ]
