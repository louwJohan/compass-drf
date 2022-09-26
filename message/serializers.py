from rest_framework import serializers
from listing.models import Listing
from .models import Message


class MessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Message
        fields = ['id', 'owner', 'listing', 'created_at',
                  'title', 'content', 'name', 'surname',
                  'phone_number', 'email']



# class MessageDetailSerializer(MessageSerializer):
#     """
#     Serializer for the Comment model used in Detail view
#     Post is a read only field so that we dont have to set it on each update
#     """
#     listing_owner = serializers.SerializerMethodField()
#     listing = serializers.ReadOnlyField(source='listing.id')
    
#     def get_listing_owner(self, obj):
#         listing_id = obj.listing.id
#         listing = Listing.objects.filter(pk=listing_id)
#         print(listing)

    