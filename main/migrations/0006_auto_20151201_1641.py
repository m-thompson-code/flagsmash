# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_bracket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bracket',
            name='playerIdList',
            field=models.CommaSeparatedIntegerField(default=b'', max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='bracket',
            name='resultsList',
            field=models.CommaSeparatedIntegerField(default=b'', max_length=255, blank=True),
        ),
    ]
