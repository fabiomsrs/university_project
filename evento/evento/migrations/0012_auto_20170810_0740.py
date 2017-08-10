# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-10 10:40
from __future__ import unicode_literals

from django.db import migrations
import enumfields.fields
import evento.models


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0011_auto_20170809_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='status',
            field=enumfields.fields.EnumField(default='novo', enum=evento.models.StatusEvento, max_length=25),
        ),
    ]
