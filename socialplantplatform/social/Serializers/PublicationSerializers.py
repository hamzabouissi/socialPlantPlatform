from rest_framework import serializers

from socialplantplatform.social.models import Publication


class PublicationListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = ("id", "user", "title", "video", "story", "created_at")


class PublicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ("id", "user", "title", "video", "story", "created_at")
