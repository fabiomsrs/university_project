# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 12:50
from __future__ import unicode_literals

import core.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comum', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField(default=0)),
                ('nome_atividade', models.CharField(max_length=25)),
                ('descricao', models.TextField(max_length=250)),
                ('tipo_atividade', enumfields.fields.EnumField(default='', enum=core.models.TipoAtividade, max_length=25)),
                ('horario_inicio', models.DateField(null=True)),
                ('horario_final', models.DateField(null=True)),
                ('ispadrao', models.BooleanField()),
                ('local', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atividades', to='comum.EspacoFisico')),
                ('usuario_criador', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='minhas_atividades', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizador', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_evento', models.CharField(max_length=25)),
                ('status', enumfields.fields.EnumField(default='novo', enum=core.models.StatusEvento, max_length=25)),
                ('tipo_evento', enumfields.fields.EnumField(default='', enum=core.models.TipoEvento, max_length=25)),
                ('data_inicio', models.DateField(null=True)),
                ('data_de_fim', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pacote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_pacote', models.CharField(max_length=25)),
                ('valor_total', models.FloatField(null=True)),
                ('atividades', models.ManyToManyField(to='core.Atividade')),
            ],
        ),
        migrations.CreateModel(
            name='Responsavel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_responsavel', models.CharField(max_length=45)),
                ('descricao_responsavel', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Trilha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('tema', models.CharField(max_length=25)),
                ('coordenadores', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EventoInscrevivel',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.Evento')),
                ('valor', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.evento', models.Model),
        ),
    ]