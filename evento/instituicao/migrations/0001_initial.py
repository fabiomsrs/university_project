# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomeInstituicao', models.CharField(max_length=25)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
    ]
