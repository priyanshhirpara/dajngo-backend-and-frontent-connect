from django.http import HttpResponse
from rest_framework import generics

from api.apis.serlizer import RoomSerializer
from api.models import Room

class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer