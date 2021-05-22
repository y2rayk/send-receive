from django.urls import path, include
from .models import Message
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'pub_date']
