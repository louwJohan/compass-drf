from django.db import IntegrityError
from rest_framework import serializers
from .models import Saved


class SavedSerializer(serializers.ModelSerializer):
    """
    Serializer for saved model
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Saved
        fields = [
            'id', 'owner', 'created_at', 'listing'
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                                               'detail': 'possible duplicate'
                                              })
