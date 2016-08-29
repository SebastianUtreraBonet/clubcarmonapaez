# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubcarmona', '0004_participantes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('enlace', models.FileField(null=True, upload_to='static/resultados')),
                ('carrera', models.ForeignKey(to='clubcarmona.Carrera')),
            ],
        ),
        migrations.RenameModel(
            old_name='Albumes',
            new_name='Albume',
        ),
        migrations.RenameModel(
            old_name='Participantes',
            new_name='Participante',
        ),
        migrations.RemoveField(
            model_name='resultados',
            name='carrera',
        ),
        migrations.DeleteModel(
            name='Resultados',
        ),
    ]
