from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from reapi.permissions import IsOwnerOrReadOnly
from .models import Message
from .serializers import MessageSerializer, MessageDetailSerializer



class MessageList(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Message.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['listing']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = MessageDetailSerializer
    queryset = Message.objects.all()