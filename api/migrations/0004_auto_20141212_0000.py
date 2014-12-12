# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20141211_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='pub_key',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'Public Key'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='signature',
            field=models.CharField(unique=True, max_length=255, verbose_name=b'Signature'),
            preserve_default=True,
        ),
    ]
