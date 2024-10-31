import requests

from rest_framework import viewsets
from rest_framework.response import Response
from .models import SpyCat, Mission
from .serializers import SpyCatSerializer, MissionSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    @action(detail=True, methods=['get'])
    def validate_breed(self, request, pk=None):
        cat = self.get_object()
        breed = cat.breed
        response = requests.get(f'https://api.thecatapi.com/v1/breeds/search?q={breed}')
        if response.status_code == 200 and response.json():
            return Response({"valid": True})
        return Response({"valid": False, "message": "Breed not recognized"}, status=400)


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def destroy(self, request, *args, **kwargs):
        mission = self.get_object()
        if mission.cat is not None:
            return Response({"error": "Cannot delete an assigned mission"}, status=400)
        return super().destroy(request, *args, **kwargs)

