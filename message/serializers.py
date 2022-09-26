from django.db import IntegrityError
from rest_framework import serializers
from listing.models import Listing
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Message
        fields = ['id', 'owner', 'listing', 'created_at',
                  'title', 'content', 'name', 'surname',
                  'phone_number', 'email']
    
    


class MessageDetailSerializer(MessageSerializer):
    """
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    listing = serializers.ReadOnlyField(source='listing.id')
    listing_owner = serializers.SerializerMethodField()

    def get_listing_owner(self, obj):
        listing = Listing.objects.filter(id=obj.listing)
        print(listing)

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })