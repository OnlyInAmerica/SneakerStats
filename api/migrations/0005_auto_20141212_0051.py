# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20141212_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peer',
            name='identifier',
            field=models.CharField(default=b'Unknown', unique=True, max_length=255, verbose_name=b'Address'),
            preserve_default=True,
        ),
    ]
