from django.db import IntegrityError
from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    

    class Meta:
        model = Message
        fields = ['id', 'owner', 'listing', 'created_at',
                  'title', 'content', 'name', 'surname', 'phone_number', 'email']
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })