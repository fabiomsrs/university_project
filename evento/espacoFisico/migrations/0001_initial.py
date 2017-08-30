# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EspacoFisico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_espaco_fisico', models.CharField(max_length=25)),
                ('espaco_fisico', models.ManyToManyField(related_name='meus_espacos_fisicos', to='espacoFisico.EspacoFisico')),
            ],
        ),
    ]
