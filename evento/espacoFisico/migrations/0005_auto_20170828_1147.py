# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 14:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('espacoFisico', '0004_auto_20170828_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='espacofisico',
            name='espaco_fisico',
            field=models.ManyToManyField(default='', related_name='meus_espacos_fisicos', to='espacoFisico.EspacoFisico'),
        ),
    ]