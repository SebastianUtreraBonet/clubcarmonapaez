# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0005_auto_20160820_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='participante',
            name='carrera',
            field=models.ForeignKey(default=0, to='clubcarmona.Carrera'),
            preserve_default=False,
        ),
    ]
