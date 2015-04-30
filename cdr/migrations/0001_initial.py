# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='VwCdr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calldate', models.DateTimeField()),
                ('src', models.CharField(max_length=80)),
                ('dst', models.CharField(max_length=80)),
                ('duration', models.TimeField(null=True, blank=True)),
                ('billsec', models.TimeField(null=True, blank=True)),
                ('disposition', models.CharField(max_length=45)),
                ('ddd', models.IntegerField(null=True, blank=True)),
                ('prefixo', models.IntegerField(null=True, blank=True)),
                ('cidade', models.CharField(max_length=100, blank=True)),
                ('estado', models.CharField(max_length=2, blank=True)),
                ('operadora', models.CharField(max_length=30, blank=True)),
                ('tipo', models.CharField(max_length=5, blank=True)),
                ('rn1', models.IntegerField(null=True, blank=True)),
                ('portado', models.CharField(max_length=3, blank=True)),
                ('preco', models.DecimalField(max_digits=10, decimal_places=3, blank=True)),
                ('userfield', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'vw_cdr',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwCidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cidade', models.CharField(max_length=100, blank=True)),
            ],
            options={
                'db_table': 'vw_cidades',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwDayStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.IntegerField(null=True, blank=True)),
                ('mes', models.IntegerField(null=True, blank=True)),
                ('total', models.BigIntegerField()),
            ],
            options={
                'db_table': 'vw_day_stats',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwDisposition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disposition', models.CharField(max_length=45)),
                ('total', models.BigIntegerField()),
            ],
            options={
                'db_table': 'vw_disposition',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwEstados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('estado', models.CharField(max_length=2, blank=True)),
                ('total', models.BigIntegerField()),
            ],
            options={
                'db_table': 'vw_estados',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwLast10',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dst', models.CharField(max_length=80)),
                ('operadora', models.CharField(max_length=30, blank=True)),
                ('tipo', models.CharField(max_length=5, blank=True)),
                ('rn1', models.IntegerField(null=True, blank=True)),
                ('calldate', models.DateTimeField()),
                ('disposition', models.CharField(max_length=45)),
                ('cidade', models.CharField(max_length=100, blank=True)),
                ('estado', models.CharField(max_length=2, blank=True)),
                ('portado', models.CharField(max_length=3, blank=True)),
            ],
            options={
                'db_table': 'vw_last_10',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwMonthStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.CharField(max_length=9, blank=True)),
                ('total', models.BigIntegerField()),
            ],
            options={
                'db_table': 'vw_month_stats',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwOperadoras',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operadora', models.CharField(max_length=64)),
                ('total', models.BigIntegerField()),
            ],
            options={
                'db_table': 'vw_operadoras',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwRamais',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ramais', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'vw_ramais',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwStatsAnswered',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.BigIntegerField(null=True, blank=True)),
                ('semana', models.BigIntegerField(null=True, blank=True)),
                ('mes', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'vw_stats_answered',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwStatsBusy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.BigIntegerField(null=True, blank=True)),
                ('semana', models.BigIntegerField(null=True, blank=True)),
                ('mes', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'vw_stats_busy',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VwStatsNoanswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('dia', models.BigIntegerField(null=True, blank=True)),
                ('semana', models.BigIntegerField(null=True, blank=True)),
                ('mes', models.BigIntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'vw_stats_noanswer',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cdr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calldate', models.DateTimeField()),
                ('clid', models.CharField(max_length=80)),
                ('src', models.CharField(max_length=80)),
                ('dst', models.CharField(max_length=80)),
                ('dcontext', models.CharField(max_length=80)),
                ('channel', models.CharField(max_length=80)),
                ('dstchannel', models.CharField(max_length=80)),
                ('lastapp', models.CharField(max_length=80)),
                ('lastdata', models.CharField(max_length=80)),
                ('duration', models.IntegerField()),
                ('billsec', models.IntegerField()),
                ('disposition', models.CharField(max_length=45)),
                ('amaflags', models.IntegerField()),
                ('accountcode', models.CharField(max_length=20)),
                ('uniqueid', models.CharField(max_length=32)),
                ('userfield', models.CharField(max_length=255)),
                ('prefix', models.CharField(max_length=80, null=True, blank=True)),
                ('portado', models.CharField(default=b'Nao', max_length=3)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Cdrport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calldate', models.DateTimeField(null=True, blank=True)),
                ('src', models.BigIntegerField(null=True, blank=True)),
                ('dst', models.BigIntegerField(null=True, blank=True)),
                ('duration', models.TimeField(null=True, blank=True)),
                ('billsec', models.TimeField(null=True, blank=True)),
                ('disposition', models.CharField(max_length=20)),
                ('ddd', models.IntegerField(null=True, blank=True)),
                ('prefixo', models.IntegerField(null=True, blank=True)),
                ('cidade', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=2)),
                ('operadora_id', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=6)),
                ('rn1_id', models.IntegerField(null=True, blank=True)),
                ('portado', models.CharField(max_length=5, blank=True)),
                ('uniqueid', models.CharField(unique=True, max_length=32, blank=True)),
                ('userfield', models.CharField(unique=True, max_length=255, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Config_Local',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ddd', models.IntegerField(help_text='Insira seu DDD', verbose_name=b'DDD')),
                ('cortar', models.IntegerField(help_text='Numero de digitos a serem cortados. Ex: Se voce envia 551120304050, digite 2 para remover o 55.', verbose_name=b'Cortar')),
                ('gravar', models.IntegerField(default=b'1', help_text='Selecione SIM, se voce grava ligacoes.', max_length=1, verbose_name=b'Audio', choices=[(b'1', b'Nao'), (b'2', b'Sim')])),
                ('custo_local', models.DecimalField(decimal_places=2, default=b'0.00', max_digits=10, blank=True, help_text='Custo Local', verbose_name=b'Fixo')),
                ('custo_ldn', models.DecimalField(decimal_places=2, default=b'0.00', max_digits=10, blank=True, help_text='Custo LDN', verbose_name=b'Fixo LDN')),
                ('custo_movel_local', models.DecimalField(decimal_places=2, default=b'0.00', max_digits=10, blank=True, help_text='Movel Local', verbose_name=b'Movel Local')),
                ('custo_movel_ldn', models.DecimalField(decimal_places=2, default=b'0.00', max_digits=10, blank=True, help_text='Movel LDN', verbose_name=b'Movel LDN')),
                ('cidade', smart_selects.db_fields.ChainedForeignKey(chained_model_field=b'id_state', chained_field=b'estado', verbose_name=b'Cidade', auto_choose=True, to='cdr.City', help_text='Selecione a cidade')),
                ('estado', models.ForeignKey(verbose_name=b'Estado', to='cdr.State', help_text='Selecione a estado')),
            ],
            options={
                'verbose_name': 'Configura\xe7\xf5es geral',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DispositionPercent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disposition', models.CharField(unique=True, max_length=30)),
                ('valor', models.IntegerField(null=True, blank=True)),
                ('perc', models.DecimalField(null=True, max_digits=10, decimal_places=2, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', models.CharField(max_length=100, blank=True)),
                ('system_number', models.CharField(max_length=100, blank=True)),
                ('system_name', models.CharField(max_length=100, blank=True)),
                ('mac', models.CharField(max_length=20, blank=True)),
                ('frequencia', models.CharField(max_length=20, blank=True)),
                ('data_ativacao', models.DateTimeField(null=True, blank=True)),
                ('data_expira', models.DateTimeField(null=True, blank=True)),
                ('ativo', models.IntegerField(default=b'1', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Prefixo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ddd', models.IntegerField(null=True, blank=True)),
                ('prefixo', models.IntegerField(unique=True, null=True, blank=True)),
                ('inicial', models.IntegerField(null=True, blank=True)),
                ('final', models.IntegerField(null=True, blank=True)),
                ('cidade', models.CharField(max_length=100, blank=True)),
                ('estado', models.CharField(max_length=2, blank=True)),
                ('operadora', models.CharField(max_length=30, blank=True)),
                ('tipo', models.CharField(max_length=5, blank=True)),
                ('rn1', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
