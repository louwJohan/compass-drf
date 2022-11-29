from rest_framework import serializers
from listing.models import Listing
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for Messages
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    listing_owner = serializers.SerializerMethodField()

    def get_listing_owner(self, obj):
        """
        Function to get listing owner
        """
        listing = Listing.objects.filter(pk=obj.listing.id)
        values = listing.values_list()
        return values[0][1]

    def get_is_owner(self, obj):
        """
        Function gets message owner
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Message
        fields = ['id', 'owner', 'listing', 'created_at',
                  'title', 'content', 'name', 'surname',
                  'phone_number', 'email', 'listing_owner']


class MessageDetailSerializer(MessageSerializer):
    """
    Serializer for the Message model used in Detail view
    """
    listing = serializers.ReadOnlyField(source='listing.id')
    listing_owner = serializers.SerializerMethodField()

    def get_listing_owner(self, obj):
        """
        Function to get listing owner
        """
        listing = Listing.objects.filter(pk=obj.listing.id)
        values = listing.values_list()
        return values[0][1]

    class Meta:
        model = Message
        fields = ['id', 'owner', 'listing', 'created_at',
                  'title', 'content', 'name', 'surname',
                  'phone_number', 'email', 'listing_owner']
