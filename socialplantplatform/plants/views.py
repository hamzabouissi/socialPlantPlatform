from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from socialplantplatform.Base.BaseSerializers import SerializerNone
from socialplantplatform.plants.models import UserPlant, Plant
from socialplantplatform.plants.serializers.PlantSerializers import PlantListSerializer, PlantCreateSerializer
from socialplantplatform.plants.serializers.UserPlantSerializers import UserPlantListSerializer, \
    UserPlantCreateSerializer


class PlantsViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializers_class = {
        "list": PlantListSerializer,
        "create": PlantCreateSerializer,
        "retrieve": PlantListSerializer,
        "update": PlantCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)


class UserPlantsViewSet(viewsets.ModelViewSet):
    queryset = UserPlant.objects.all()
    serializers_class = {
        "list": UserPlantListSerializer,
        "create": UserPlantCreateSerializer,
        "retrieve": UserPlantListSerializer,
        "update": UserPlantCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)
