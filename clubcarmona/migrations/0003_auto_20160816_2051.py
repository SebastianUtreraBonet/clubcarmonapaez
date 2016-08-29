# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0002_auto_20160726_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrera',
            name='precio',
            field=models.FloatField(default=0, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='texto',
            field=ckeditor.fields.RichTextField(null=True, max_length=99999999, blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now, blank=True, null=True),
        ),
    ]
