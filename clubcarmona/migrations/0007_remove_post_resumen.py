# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-07-22 11:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0006_albumes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='resumen',
        ),
    ]
