# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20151201_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bracket',
            name='playerIdList',
        ),
        migrations.RemoveField(
            model_name='bracket',
            name='resultsList',
        ),
    ]
