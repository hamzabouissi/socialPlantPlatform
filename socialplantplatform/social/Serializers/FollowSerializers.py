from django.contrib.auth import get_user_model
from rest_framework import serializers

from socialplantplatform.social.models import UserFollow

User = get_user_model()

class InnerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","username", "image")


class FollowCreateSerializer(serializers.ModelSerializer):
    follow_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserFollow
        fields = ("id", "follow_by", "follow_to")


class FollowToSerializer(serializers.ModelSerializer):
    follow_to = InnerUserSerializer()
    class Meta:
        model = UserFollow
        fields = ("id", "follow_to")


class FollowMetListSerializer(serializers.ModelSerializer):
    follow_by = InnerUserSerializer()

    class Meta:
        model = UserFollow
        fields = ("id", "follow_by",)
