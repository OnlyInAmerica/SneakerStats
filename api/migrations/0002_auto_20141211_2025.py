# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='peer',
            name='address',
        ),
        migrations.AddField(
            model_name='peer',
            name='identifier',
            field=models.CharField(default=b'Unknown', max_length=255, verbose_name=b'Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='session',
            name='platform',
            field=models.CharField(default=b'Unknown', max_length=255, verbose_name=b'Client Platform'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='session',
            name='role',
            field=models.CharField(default=b'Unknown', max_length=255, verbose_name=b'Role (Central, Peripheral)'),
            preserve_default=True,
        ),
    ]
