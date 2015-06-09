# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20150608_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servercliente',
            name='ativacao',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
