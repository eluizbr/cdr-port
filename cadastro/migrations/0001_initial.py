# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=10, verbose_name='Tipo', choices=[(b'fisca', b'Pessoa Fisca'), (b'jurica', b'Pessoa Jurica')])),
                ('cpf', models.CharField(max_length=20, verbose_name='CPF')),
                ('cnpj', models.CharField(max_length=20, verbose_name='CNPJ')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('endereco', models.CharField(max_length=100, verbose_name='Endere\xe7o')),
                ('numero', models.CharField(max_length=100, verbose_name='N\xfamero')),
                ('complemento', models.CharField(max_length=100, verbose_name='Complento')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('cod_cliente', models.IntegerField(max_length=100, verbose_name='Codigo do Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServerCliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome_servidor', models.CharField(max_length=100, verbose_name='Nome do servidor')),
                ('ip_servidor', models.CharField(max_length=100, verbose_name='IP do servidor')),
                ('plano', models.CharField(max_length=100, verbose_name='Plano do servidor')),
                ('id_cliente', models.OneToOneField(to='cadastro.Cadastro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
