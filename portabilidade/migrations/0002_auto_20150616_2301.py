# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portabilidade', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ipspermitidos',
            old_name='ip',
            new_name='ipaddr',
        ),
    ]
