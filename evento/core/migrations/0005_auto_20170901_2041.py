# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-01 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170901_1954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pacote',
            name='pacote',
        ),
        migrations.RemoveField(
            model_name='trilha',
            name='atividades',
        ),
        migrations.RemoveField(
            model_name='trilha',
            name='id',
        ),
        migrations.RemoveField(
            model_name='trilha',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='trilha',
            name='usuario_criador',
        ),
        migrations.RemoveField(
            model_name='trilha',
            name='valor',
        ),
        migrations.AddField(
            model_name='pacote',
            name='atividades',
            field=models.ManyToManyField(to='core.Atividade'),
        ),
        migrations.AddField(
            model_name='trilha',
            name='pacote_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Pacote'),
            preserve_default=False,
        ),
    ]
