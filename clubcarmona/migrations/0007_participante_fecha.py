# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0006_participante_carrera'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 20, 20, 51, 2, 910993)),
        ),
    ]
