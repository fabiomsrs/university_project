# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0003_auto_20170830_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='valor',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='eventoinscrevivel',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]