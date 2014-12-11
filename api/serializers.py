#from django.contrib.auth.models import User, Group
from models import Session
from rest_framework import serializers


class SessionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Session
        #fields = ('url', 'username', 'email', 'groups')