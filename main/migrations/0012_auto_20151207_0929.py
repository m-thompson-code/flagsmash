# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20151207_0916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='player',
            old_name='tag',
            new_name='name',
        ),
    ]
