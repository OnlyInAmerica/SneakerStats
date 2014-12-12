# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20141211_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='identitytransmission',
            old_name='end_time',
            new_name='stop_time',
        ),
        migrations.RenameField(
            model_name='messagetransmission',
            old_name='end_time',
            new_name='stop_time',
        ),
    ]
