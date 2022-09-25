from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    

    class Meta:
        model = Message
        fields = ['id', 'owner', 'listing', 'created_at',
                  'title', 'content', 'name', 'surname', 'phone_number', 'email']