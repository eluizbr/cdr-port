# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('portabilidade', '0002_auto_20150616_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipspermitidos',
            name='key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
    ]
