# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0012_auto_20160823_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos_carrera',
            name='enlace1',
            field=models.CharField(max_length=9999),
        ),
        migrations.AlterField(
            model_name='fotos_carrera',
            name='enlace2',
            field=models.CharField(blank=True, null=True, max_length=9999),
        ),
        migrations.AlterField(
            model_name='fotos_carrera',
            name='enlace3',
            field=models.CharField(blank=True, null=True, max_length=9999),
        ),
        migrations.AlterField(
            model_name='participante',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 19, 27, 24, 912297)),
        ),
    ]
