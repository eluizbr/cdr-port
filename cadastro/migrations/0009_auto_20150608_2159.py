# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20150608_2154'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cidade', models.CharField(max_length=100, blank=True)),
                ('estado', models.CharField(max_length=2, blank=True)),
                ('ddd', models.IntegerField(null=True, blank=True)),
                ('regiao', models.CharField(max_length=25, blank=True)),
            ],
            options={
                'db_table': 'cidades',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cidade', models.CharField(max_length=50)),
                ('iso', models.IntegerField()),
                ('iso_ddd', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_region', models.IntegerField()),
                ('title', models.CharField(max_length=35)),
                ('letter', models.CharField(max_length=2)),
                ('iso', models.IntegerField()),
                ('created_at', models.DateTimeField(null=True, blank=True)),
                ('updated_at', models.DateTimeField(null=True, blank=True)),
                ('status', models.CharField(max_length=1)),
            ],
            options={
                'db_table': 'state',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='estado',
            field=models.ForeignKey(blank=True, to='cadastro.State', help_text='Selecione a estado', null=True, verbose_name=b'Estado'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='cidade',
            field=smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'id_state', chained_field=b'estado', verbose_name=b'Cidade', auto_choose=True, to='cadastro.City', help_text='Selecione a cidade'),
            preserve_default=True,
        ),
    ]
