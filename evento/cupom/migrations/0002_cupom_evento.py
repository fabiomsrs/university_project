# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-25 21:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evento', '0001_initial'),
        ('cupom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupom',
            name='evento',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='meus_cupons', to='evento.Evento'),
        ),
    ]