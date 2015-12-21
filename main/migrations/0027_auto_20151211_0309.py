# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20151211_0308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playermatch',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=None, null=True, blank=True),
        ),
    ]
