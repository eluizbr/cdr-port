# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20150608_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='servercliente',
            name='ativacao',
            field=models.DateTimeField(default=datetime.datetime.now, auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servercliente',
            name='plano',
            field=models.CharField(default=b'Free', max_length=100, verbose_name='Plano do servidor', choices=[(b'Free', b'Free'), (b'Premium', b'Premium')]),
            preserve_default=True,
        ),
    ]
