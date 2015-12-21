# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_auto_20151213_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='challongetournament',
            name='description',
            field=models.CharField(default=b'', max_length=200, blank=True),
        ),
    ]
