# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0014_auto_20160824_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='resultado',
            field=models.FileField(upload_to='static/resultados', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='participante',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 18, 10, 3, 301881)),
        ),
    ]
