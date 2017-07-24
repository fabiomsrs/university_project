# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-24 13:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('evento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cupom',
            name='inscricao',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuario.Inscricao'),
        ),
        migrations.AddField(
            model_name='evento',
            name='usuarioCriador',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='usuario.Usuario'),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='inscricao',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='usuario.Inscricao'),
        ),
    ]
