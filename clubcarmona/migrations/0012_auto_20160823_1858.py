# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0011_auto_20160820_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fotos_Carrera',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('enlace1', models.TextField()),
                ('enlace2', models.TextField(blank=True, null=True)),
                ('enlace3', models.TextField(blank=True, null=True)),
                ('carrera', models.ForeignKey(to='clubcarmona.Carrera')),
            ],
        ),
        migrations.AlterField(
            model_name='participante',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 23, 18, 58, 44, 946200)),
        ),
    ]
