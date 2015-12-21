# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20151212_0349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playersync',
            name='created_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='playersync',
            name='updated_at',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
