# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0003_auto_20160816_2051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participantes',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lista', ckeditor.fields.RichTextField(max_length=99999999, null=True, blank=True)),
            ],
        ),
    ]
