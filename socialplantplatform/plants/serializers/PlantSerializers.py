from rest_framework import serializers

from socialplantplatform.plants.models import Plant


class PlantListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plant
        fields = ("id", "name", "description", "image")


class PlantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = ("id", "name", "description", "image")



