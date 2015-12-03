# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20151201_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bracket',
            old_name='playerIdJSON',
            new_name='dataJSON',
        ),
        migrations.RemoveField(
            model_name='bracket',
            name='resultsJSON',
        ),
    ]
