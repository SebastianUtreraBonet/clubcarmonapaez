# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0024_auto_20160825_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liga',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('lista', ckeditor.fields.RichTextField(blank=True, max_length=99999999, null=True)),
                ('fecha', models.DateTimeField(default=datetime.datetime(2016, 9, 2, 14, 8, 18, 852503))),
            ],
        ),
        migrations.AlterField(
            model_name='participante',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 2, 14, 8, 18, 851498)),
        ),
    ]
