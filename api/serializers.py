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