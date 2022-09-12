from rest_framework import generics, permissions
from reapi.permissions import IsOwnerOrReadOnly
from .models import Message
from .serializers import MessageSerializer


class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Message.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MessageDetail(generics.RetrieveDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MessageSerializer
    queryset = Message.objects.all()