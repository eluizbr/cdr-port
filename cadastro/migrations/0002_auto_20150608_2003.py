# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servercliente',
            name='id_cliente',
            field=models.ForeignKey(to='cadastro.Cadastro', db_column=b'cod_cliente'),
            preserve_default=True,
        ),
    ]
