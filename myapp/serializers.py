from .models import Message
from rest_framework_json_api import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'text', 'receiver', 'seen', 'pub_date']
