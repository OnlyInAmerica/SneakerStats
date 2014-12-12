#from django.contrib.auth.models import User, Group
from models import Session, Identity, Message, Peer, MessageTransmission, IdentityTransmission
from rest_framework import serializers


class IdentitySerializer(serializers.Serializer):

    pub_key = serializers.CharField(max_length=255)

    class Meta:
        model = Identity


class MessageSerializer(serializers.Serializer):

    signature = serializers.CharField(max_length=255)

    class Meta:
        model = Message


class PeerSerializer(serializers.Serializer):

    identifier = serializers.CharField(max_length=255)

    class Meta:
        model = Peer


class MessageTransmissionSerializer(serializers.ModelSerializer):

    message = MessageSerializer()

    class Meta:
        model = MessageTransmission


class IdentityTransmissionSerializer(serializers.ModelSerializer):

    identity = IdentitySerializer()

    class Meta:
        model = IdentityTransmission


class SessionSerializer(serializers.ModelSerializer):

    local_peer = PeerSerializer()
    remote_peer = PeerSerializer()
    identities_written = IdentityTransmissionSerializer(many=True)
    identities_read = IdentityTransmissionSerializer(many=True)
    messages_written = MessageTransmissionSerializer(many=True)
    messages_read = MessageTransmissionSerializer(many=True)

    class Meta:
        model = Session
        depth = 3
        #fields = ('url', 'username', 'email', 'groups')

    def create(self, validated_data):

        local_peer_data = validated_data.pop('local_peer')
        local_peer, created = Peer.objects.get_or_create(identifier=local_peer_data['identifier'])

        remote_peer_data = validated_data.pop('remote_peer')
        remote_peer, created = Peer.objects.get_or_create(identifier=remote_peer_data['identifier'])

        ids_written_data = validated_data.pop('identities_written')
        ids_written = []
        for id_written_data in ids_written_data:
            id_written = createIdentityTransmissionFromDict(id_written_data)
            ids_written.append(id_written)

        ids_read_data = validated_data.pop('identities_read')
        ids_read = []
        for id_read_data in ids_read_data:
            id_read = createIdentityTransmissionFromDict(id_read_data)
            ids_read.append(id_read)

        msgs_written_data = validated_data.pop('messages_written')
        msgs_written = []
        for msg_written_data in msgs_written_data:
            msg_written = createMessageTransmissionFromDict(msg_written_data)
            msgs_written.append(msg_written)

        msgs_read_data = validated_data.pop('messages_read')
        msgs_read = []
        for msg_read_data in msgs_read_data:
            msg_read = createMessageTransmissionFromDict(msg_read_data)
            msgs_read.append(msg_read)

        validated_data['local_peer'] = local_peer
        validated_data['remote_peer'] = remote_peer

        session = Session.objects.create(**validated_data)

        session.local_peer = local_peer
        session.remote_peer = remote_peer
        session.identities_read = ids_read
        session.identities_written = ids_written
        session.messages_read = msgs_read
        session.messages_written = msgs_written

        return session


def createIdentityTransmissionFromDict(dict):
    id, created = Identity.objects.get_or_create(pub_key=dict['identity']['pub_key'])

    id_xmit = IdentityTransmission.objects.create(identity=id)
    id_xmit = assignTransmissionValuesFromDict(id_xmit, dict)
    return id_xmit


def createMessageTransmissionFromDict(dict):
    msg, created = Message.objects.get_or_create(signature=dict['message']['signature'])

    msg_xmit = MessageTransmission.objects.create(message=msg)
    msg_xmit = assignTransmissionValuesFromDict(msg_xmit, dict)
    return msg_xmit


def assignTransmissionValuesFromDict(transmission, dict):
    transmission.successful = dict['successful']
    transmission.start_time = dict['start_time']
    transmission.stop_time = dict['stop_time']
    transmission.save()
    return transmission