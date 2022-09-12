from rest_framework import generics
from reapi.permissions import IsOwnerOrReadOnly
from .serializers import ProfileSerializer
from .models import Profile


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
        
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]