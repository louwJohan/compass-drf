from rest_framework import serializers
from message.models import Message
from follow.models import Follower
from listing.models import Listing
from saved.models import Saved
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Profile model serializer
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    listing_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()
    listings = serializers.SerializerMethodField()
    saved_count = serializers.SerializerMethodField()
    saved = serializers.SerializerMethodField()
    messages_count = serializers.SerializerMethodField()
    messages = serializers.SerializerMethodField()

    def get_saved_count(self, obj):
        """
        Function gets amount of saved listings
        """
        saved = Saved.objects.filter(owner=obj.owner)
        return (len(saved))

    def get_messages_count(self, obj):
        """
        Function gets amount of messages
        """
        messages = Message.objects.all()
        message_list = []
        listings = Listing.objects.filter(owner=obj.owner)
        listing_list = []
        for listing in listings:
            listing_list.append(listing.id)
        for message in messages:
            if message.listing.id in listing_list:
                message_list.append(message.id)
        return len(message_list)

    def get_messages(self, obj):
        """
        Function gets all messages that was sent to profile
        owner
        """
        messages = Message.objects.all()
        message_list = []
        listings = Listing.objects.filter(owner=obj.owner)
        listing_list = []
        for listing in listings:
            listing_list.append(listing.id)
        for message in messages:
            if message.listing.id in listing_list:
                message_list.append(message.id)
        return message_list

    def get_saved(self, obj):
        """
        function gets saved listings
        """
        saved = Saved.objects.filter(owner=obj.owner)
        saved_list = []
        for item in saved:
            saved_list.append(item.listing.id)
        return saved_list

    def get_listings(self, obj):
        """
        Function gets profile owners listings
        """
        listings = Listing.objects.filter(owner=obj.owner)
        listing_list = []
        for listing in listings:
            listing_list.append(listing.id)
        return listing_list

    def get_is_owner(self, obj):
        """
        Function checks if user is owner of profile
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        """
        Function gets ID of user following profile
        """
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(owner=user,
                                                followed=obj.owner
                                                ).first()
            return following.id if following else None
        return None

    class Meta:
        model = Profile
        fields = ['id', 'owner', 'created_at', 'updated_at', 'profile_name',
                  'profile_content', 'profile_image', 'is_owner',
                  'following_id', 'listing_count', 'followers_count',
                  'following_count', 'listings', 'saved_count', 'saved',
                  'messages_count', 'messages'
                  ]
