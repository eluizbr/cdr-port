# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_servercliente_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='servercliente',
            name='setup',
            field=models.IntegerField(default=b'0', max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='cnpj',
            field=models.CharField(max_length=20, null=True, verbose_name='CNPJ', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='cpf',
            field=models.CharField(max_length=20, null=True, verbose_name='CPF', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servercliente',
            name='status',
            field=models.CharField(max_length=10, verbose_name='Ativo', choices=[(b'Sim', b'Sim'), (b'Nao', b'Nao')]),
            preserve_default=True,
        ),
    ]
