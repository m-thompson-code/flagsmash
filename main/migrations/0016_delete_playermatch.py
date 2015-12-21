# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20151208_0013'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PlayerMatch',
        ),
    ]
