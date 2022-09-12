from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from reapi.permissions import IsOwnerOrReadOnly
from .models import Listing
from .serializers import ListingSerializer


class ListingList(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Listing.objects.annotate(
        saved_count=Count('saved', distinct=True),
        messages_count=Count('message', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'owner__followed__owner__profile',
        'saved__owner__profile',
        'owner__profile',
    ]

    search_fields = [
        'owner__username',
        'title',
        'bedrooms',
        'area',
        'type_of_property',
        'price',

    ]
    ordering_fields = [
        'saved_count',
        'messages_count',
        'saved__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ListingSerializer
    queryset = Listing.objects.annotate(
        saved_count=Count('saved', distinct=True),
        messages_count=Count('message', distinct=True)
    ).order_by('-created_at')
