# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pabx', '0002_auto_20150515_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rt_calls',
            name='controle',
            field=models.IntegerField(default=0, max_length=1, null=True, blank=True),
            preserve_default=True,
        ),
    ]
