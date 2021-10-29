from rest_framework import serializers

from socialplantplatform.plants.models import UserPlant


class UserPlantListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserPlant
        fields = ("id", "user", "plant", "price")


class UserPlantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlant
        fields = ("id", "user", "plant", "price")
