# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pabx', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rt_calls',
            name='controle',
            field=models.IntegerField(default=0, max_length=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='rt_calls',
            name='Duration',
            field=models.TimeField(),
            preserve_default=True,
        ),
    ]
