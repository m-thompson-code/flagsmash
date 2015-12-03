# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20151127_0118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bracket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'')),
                ('playerIdList', models.CommaSeparatedIntegerField(default=b'', max_length=64, blank=True)),
                ('resultsList', models.CommaSeparatedIntegerField(default=b'', max_length=64, blank=True)),
            ],
        ),
    ]
