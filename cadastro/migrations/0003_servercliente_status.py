# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20150608_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='servercliente',
            name='status',
            field=models.CharField(default=b'N\xc3\xa3o', max_length=10, verbose_name='Status', choices=[(b'Sim', b'Sim'), (b'N\xc3\xa3o', b'N\xc3\xa3o')]),
            preserve_default=True,
        ),
    ]
