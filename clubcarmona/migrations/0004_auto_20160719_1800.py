# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-19 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0003_auto_20160719_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='resumen',
            field=models.TextField(default=' ', max_length=350, null=True),
        ),
    ]
