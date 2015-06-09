# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_auto_20150608_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='bairro',
            field=models.CharField(max_length=100, null=True, verbose_name='Bairro', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name=b'Email', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='telefone',
            field=models.CharField(max_length=20, null=True, verbose_name='Telefone', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='nome',
            field=models.CharField(max_length=100, null=True, verbose_name='Nome', blank=True),
            preserve_default=True,
        ),
    ]
