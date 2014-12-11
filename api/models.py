from django.db import models

# Create your models here.


class Identity(models.Model):

    alias = models.CharField('Alias', max_length=255, blank=True)
    pub_key = models.CharField('Public Key', max_length=255)


class Message(models.Model):

    signature = models.CharField('Signature', max_length=255, blank=True)


class Transmission(models.Model):

    successful = models.BooleanField('Successful', default=True)
    start_time = models.DateTimeField('Start Time', blank=True, null=True)
    end_time = models.DateTimeField('Stop Time', blank=True, null=True)

    class Meta:
        abstract = True


class MessageTransmission(Transmission):

    message = models.ForeignKey(Message)


class IdentityTransmission(Transmission):

    identity = models.ForeignKey(Identity)


class Peer(models.Model):

    identifier = models.CharField('Address', max_length=255, default='Unknown')


class Session(models.Model):

    version = models.IntegerField('Model Version', default=1)
    platform = models.CharField('Client Platform', max_length=255, default='Unknown')
    role = models.CharField('Role (Central, Peripheral)', max_length=255, default='Unknown')

    local_peer = models.ForeignKey(Peer, related_name='initiated_session')
    remote_peer = models.ForeignKey(Peer, related_name='received_session')

    lat = models.FloatField('Local Peer Latitude', blank=True, null=True)
    lon = models.FloatField('Local Peer Longitude', blank=True, null=True)

    start_time = models.DateTimeField('Session Start Time', blank=True, null=True)
    stop_time = models.DateTimeField('Session Stop Time', blank=True, null=True)

    identities_written = models.ManyToManyField(IdentityTransmission, related_name='written_during_session')
    identities_read = models.ManyToManyField(IdentityTransmission, related_name='read_during_session')

    messages_written = models.ManyToManyField(MessageTransmission, related_name='written_during_session')
    messages_read = models.ManyToManyField(MessageTransmission, related_name='read_during_Session')

