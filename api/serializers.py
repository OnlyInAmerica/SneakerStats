#from django.contrib.auth.models import User, Group
from models import Session, Identity, Message, Peer, MessageTransmission, IdentityTransmission
from rest_framework import serializers


class IdentitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Identity


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message


class PeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peer


class MessageTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MessageTransmission


class IdentityTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentityTransmission


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        depth = 2
        #fields = ('url', 'username', 'email', 'groups')

    def create(self, validated_data):
        local_peer_data = validated_data.pop('local_peer')
        local_peer = Peer.objects.create(**local_peer_data)

        remote_peer_data = validated_data.pop('remote_peer')
        remote_peer = Peer.objects.create(**remote_peer_data)

        session = Session.objects.create(**validated_data)

        session.local_peer = local_peer
        session.remote_peer = remote_peer

        return session