# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 02:04
from __future__ import unicode_literals

from django.db import migrations
import enumfields.fields
import evento.models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0010_auto_20170809_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='tipo_evento',
            field=enumfields.fields.EnumField(default='congresso', enum=evento.models.TipoEvento, max_length=25),
        ),
    ]
