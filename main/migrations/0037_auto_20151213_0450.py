# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20151212_0503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playermatch',
            options={'ordering': ['created_at', 'identifier']},
        ),
    ]
