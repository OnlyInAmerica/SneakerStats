# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alias', models.CharField(max_length=255, verbose_name=b'Alias', blank=True)),
                ('pub_key', models.CharField(max_length=255, verbose_name=b'Public Key')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IdentityTransmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('successful', models.BooleanField(default=True, verbose_name=b'Successful')),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'Start Time', blank=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name=b'Stop Time', blank=True)),
                ('identity', models.ForeignKey(to='api.Identity')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('signature', models.CharField(max_length=255, verbose_name=b'Signature', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MessageTransmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('successful', models.BooleanField(default=True, verbose_name=b'Successful')),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'Start Time', blank=True)),
                ('end_time', models.DateTimeField(null=True, verbose_name=b'Stop Time', blank=True)),
                ('message', models.ForeignKey(to='api.Message')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Peer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255, verbose_name=b'Address', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('version', models.IntegerField(default=1, verbose_name=b'Model Version')),
                ('lat', models.FloatField(null=True, verbose_name=b'Local Peer Latitude', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name=b'Local Peer Longitude', blank=True)),
                ('start_time', models.DateTimeField(null=True, verbose_name=b'Session Start Time', blank=True)),
                ('stop_time', models.DateTimeField(null=True, verbose_name=b'Session Stop Time', blank=True)),
                ('identities_read', models.ManyToManyField(related_name='read_during_session', to='api.IdentityTransmission')),
                ('identities_written', models.ManyToManyField(related_name='written_during_session', to='api.IdentityTransmission')),
                ('local_peer', models.ForeignKey(related_name='initiated_session', to='api.Peer')),
                ('messages_read', models.ManyToManyField(related_name='read_during_Session', to='api.MessageTransmission')),
                ('messages_written', models.ManyToManyField(related_name='written_during_session', to='api.MessageTransmission')),
                ('remote_peer', models.ForeignKey(related_name='received_session', to='api.Peer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
