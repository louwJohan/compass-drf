from django.db.models import Count
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from reapi.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile


class ProfileList(generics.ListAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        listing_count=Count('owner__listing', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__following__followed__profile',
    ]
    
    ordering_fields = [
        'listing_count',
        'followers_count',
        'following_count',
        'owner__following__created_at',
        'owner__followed__created_at',
    ]
        
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        listing_count=Count('owner__listing', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True)
    ).order_by('-created_at')