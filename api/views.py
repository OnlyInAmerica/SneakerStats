from django.shortcuts import render
from rest_framework import viewsets
from models import Session
from serializers import SessionSerializer

# Create your views here.

class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Sessions to be viewed or submitted.
    """
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
