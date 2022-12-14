from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from saved.models import Saved
from .models import Listing


class ListingSerializer(serializers.ModelSerializer):
    """
    Serializer for Listings model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()
    saved_id = serializers.SerializerMethodField()
    saved_count = serializers.ReadOnlyField()
    messages_count = serializers.ReadOnlyField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url',
                                              default='../default_profile_ik0b2z.jpg') 

    def get_is_owner(self, obj):
        """
        Function to get owner of listing
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        """
        Function to get time and date when listing
        was created
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Function to get time and date when listing was
        updated
        """
        return naturaltime(obj.updated_at)

    def get_saved_id(self, obj):
        """
        Function to get ID of user that saved the listing
        """
        user = self.context['request'].user
        if user.is_authenticated:
            saved = Saved.objects.filter(
                owner=user, listing=obj
            ).first()
            return saved.id if saved else None
        return None

    class Meta:
        """
        Setting fields for serializer
        """
        model = Listing
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title',
            'is_owner', 'description', 'type_of_property',
            'bedrooms', 'area', 'price', 'commerce_type', 'saved_id',
            'image_one', 'image_two', 'image_three', 'image_three',
            'image_four', 'image_five', 'image_six', 'image_seven',
            'image_eight', 'saved_id', 'saved_count', 'messages_count',
            'profile_image', 'profile_id'
            ]
