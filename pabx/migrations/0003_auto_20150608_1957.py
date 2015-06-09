# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pabx', '0002_auto_20150522_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='rt_calls',
            name='callerid',
            field=models.CharField(max_length=40, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sip',
            name='allow',
            field=models.CharField(default=b'ulaw,alaw,gsm,g729', max_length=40, verbose_name='Codec', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sip',
            name='ipaddr',
            field=models.CharField(default=b'0.0.0.0', max_length=15, verbose_name='IP', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sip',
            name='name',
            field=models.CharField(unique=True, max_length=10, verbose_name='Ramal'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='sip',
            name='secret',
            field=models.CharField(max_length=40, verbose_name='Senha', blank=True),
            preserve_default=True,
        ),
    ]
