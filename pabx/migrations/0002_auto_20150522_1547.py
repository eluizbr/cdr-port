# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pabx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VwCall',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('origem', models.CharField(max_length=50, blank=True)),
                ('destino', models.CharField(max_length=100, blank=True)),
                ('ramal', models.CharField(max_length=10)),
                ('ip', models.CharField(max_length=15)),
                ('lastms', models.IntegerField(null=True, blank=True)),
                ('status', models.CharField(max_length=10, blank=True)),
                ('tempo', models.TimeField()),
                ('controle', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'vw_call',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rt_calls',
            name='ipaddr',
            field=models.CharField(max_length=15, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rt_calls',
            name='lastms',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rt_calls',
            name='BridgeId',
            field=models.CharField(max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rt_calls',
            name='Uniqueid',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
