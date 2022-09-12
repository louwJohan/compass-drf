from rest_framework import generics, permissions
from reapi.permissions import IsOwnerOrReadOnly
from .models import Saved
from .serializers import SavedSerializer


class SavedList(generics.ListCreateAPIView):
    serializer_class = SavedSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Saved.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class SavedDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = SavedSerializer
    queryset = Saved.objects.all()