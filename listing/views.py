from rest_framework import generics, permissions
from reapi.permissions import IsOwnerOrReadOnly
from .models import Listing
from .serializers import ListingSerializer


class ListingList(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Listing.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ListingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()
