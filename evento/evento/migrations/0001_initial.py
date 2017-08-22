# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-22 10:52
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import enumfields.fields
import evento.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_atividade', models.CharField(max_length=25)),
                ('descricao', models.TextField(max_length=250)),
                ('valor_atividade', models.FloatField(null=True)),
                ('tipo_atividade', enumfields.fields.EnumField(default='', enum=evento.models.TipoAtividade, max_length=25)),
                ('local', models.CharField(max_length=100)),
                ('ispadrao', models.BooleanField()),
                ('usuario_criador', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='minhas_atividades', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckIn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organizador', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cupom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cupom', models.CharField(max_length=50)),
                ('desconto', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('isautomatico', models.BooleanField()),
                ('data_de_inicio', models.DateTimeField()),
                ('data_de_fim', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_evento', models.CharField(max_length=25)),
                ('status', enumfields.fields.EnumField(default='novo', enum=evento.models.StatusEvento, max_length=25)),
                ('tipo_evento', enumfields.fields.EnumField(default='', enum=evento.models.TipoEvento, max_length=25)),
                ('membros', models.ManyToManyField(related_name='meus_eventos', to=settings.AUTH_USER_MODEL)),
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
    ]
