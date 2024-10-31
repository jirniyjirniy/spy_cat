import requests

from rest_framework import viewsets
from rest_framework.response import Response
from .models import SpyCat, Mission, Target
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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def complete_target(self, request, pk=None, target_pk=None):
        mission = self.get_object()
        target = get_object_or_404(Target, id=target_pk, mission=mission)

        if target.is_complete:
            return Response({"error": "Target is already completed"}, status=400)

        target.is_complete = True
        target.save()

        if all(target.is_complete for target in mission.targets.all()):
            mission.is_complete = True
            mission.save()

        return Response({"message": "Target marked as complete"}, status=200)
