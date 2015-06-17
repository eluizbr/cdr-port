# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NaoPortados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operadora', models.CharField(max_length=64)),
                ('tipo', models.CharField(max_length=64)),
                ('prefixo', models.BigIntegerField()),
                ('rn1', models.IntegerField()),
            ],
            options={
                'db_table': 'nao_portados',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Portados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numero', models.BigIntegerField()),
                ('rn1', models.IntegerField()),
                ('data_hora', models.DateTimeField()),
                ('op', models.IntegerField()),
            ],
            options={
                'db_table': 'portados',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IpsPermitidos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.GenericIPAddressField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
