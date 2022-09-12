from rest_framework import generics
from .serializers import ProfileSerializer
from reapi.permissions import IsOwnerOrReadOnly
from .models import Profile

class ProfileList(generics.ListCreateAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
        
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsOwnerOrReadOnly]