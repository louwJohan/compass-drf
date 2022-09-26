from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from saved.models import Saved
from .models import Listing

def validate(value):
    if value.size > 1024 * 1024 * 2:
        raise serializers.ValidationError(
                'Image size larger than 2MB'
        )
    if value.image.width > 4096:
        raise serializers.ValidationError(
                'Image width larger than 4096px'
        )
    if value.image.height > 4096:
        raise serializers.ValidationError(
                'Image height larger than 4096px'
        )
    return value

class ListingSerializer(serializers.ModelSerializer):
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
    image_one = serializers.ImageField(validators=[validate])
    image_two = serializers.ImageField(validators=[validate])
    image_three = serializers.ImageField(validators=[validate])
    image_four = serializers.ImageField(validators=[validate])
    image_five = serializers.ImageField(validators=[validate])
    image_six = serializers.ImageField(validators=[validate])
    image_seven = serializers.ImageField(validators=[validate])
    image_eight = serializers.ImageField(validators=[validate])

    

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    
    def get_saved_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            saved = Saved.objects.filter(
                owner=user, listing=obj
            ).first()
            return saved.id if saved else None
        return None

    class Meta:
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
