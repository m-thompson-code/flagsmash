# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20151201_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='bracket',
            name='playerIdJSON',
            field=jsonfield.fields.JSONField(default={}),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bracket',
            name='resultsJSON',
            field=jsonfield.fields.JSONField(default=[]),
            preserve_default=False,
        ),
    ]
