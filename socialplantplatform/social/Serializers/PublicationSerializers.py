from rest_framework import serializers

from socialplantplatform.plants.models import User
from socialplantplatform.social.models import Publication

# Inner Serializers
class InnerUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "image")
        ref_name = "publication"



class PublicationListSerializer(serializers.ModelSerializer):
    user = InnerUserSerializer()
    class Meta:
        model = Publication
        fields = ("id", "user", "title","image", "video", "story", "sell", "quantity","expired", "created_at")


class PublicationCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Publication
        fields = ("id", "user", "title","image", "video", "story", "sell", "quantity", "created_at")


class FriendsPublicationListSerializer(serializers.ModelSerializer):
    user = InnerUserSerializer()

    class Meta:
        model = Publication
        fields = ("id", "user", "title", "image", "sell", "quantity", "created_at")


# Stories

class PublicationStoriesListSerializer(serializers.ModelSerializer):
    user = InnerUserSerializer()

    class Meta:
        model = Publication
        fields = ("id", "user", "title", "video", "sell", "quantity", "created_at")
