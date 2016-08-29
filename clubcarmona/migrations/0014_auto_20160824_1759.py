# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0013_auto_20160823_1927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fotos_carrera',
            name='carrera',
        ),
        migrations.RemoveField(
            model_name='resultado',
            name='carrera',
        ),
        migrations.AddField(
            model_name='carrera',
            name='galeria_fotos_1',
            field=models.CharField(max_length=9999, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='carrera',
            name='galeria_fotos_2',
            field=models.CharField(max_length=9999, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='carrera',
            name='galeria_fotos_3',
            field=models.CharField(max_length=9999, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='carrera',
            name='resultado',
            field=models.FileField(upload_to='static/resultados', null=True),
        ),
        migrations.AlterField(
            model_name='participante',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 24, 17, 59, 58, 546145)),
        ),
        migrations.DeleteModel(
            name='Fotos_Carrera',
        ),
        migrations.DeleteModel(
            name='Resultado',
        ),
    ]
