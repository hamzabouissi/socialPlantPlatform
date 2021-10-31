from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from socialplantplatform.Base.BaseSerializers import SerializerNone
from socialplantplatform.social.Serializers.FollowSerializers import FollowToSerializer, FollowCreateSerializer,FollowMetListSerializer
from socialplantplatform.social.Serializers.PublicationSerializers import PublicationListSerializer, \
    PublicationCreateSerializer, PublicationStoriesListSerializer, FriendsPublicationListSerializer
from socialplantplatform.social.filters import PublicationFilter
from socialplantplatform.social.models import Publication, UserFollow
from socialplantplatform.social.permissions import UserOwnPublication


class PublicationViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    serializers_class = {
        "list": PublicationListSerializer,
        "create": PublicationCreateSerializer,
        "retrieve": PublicationListSerializer,
        "update": PublicationCreateSerializer,
        "friends_stories": PublicationStoriesListSerializer,
        "friends_publications": FriendsPublicationListSerializer
    }
    filterset_class = PublicationFilter
    queryset = Publication.objects.all()
    permission_classes = (IsAuthenticated,UserOwnPublication,)

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)

    @action(detail=False, methods=['get'],filterset_class=None)
    def friends_publications(self, request, *args, **kwargs):
        queryset = Publication.objects.get_user_follows_publications(request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


    @action(detail=False, methods=['get'],filterset_class=None)
    def friends_stories(self, request, *args, **kwargs):
        queryset = Publication.objects.get_user_follows_stories(request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FollowViewSet(viewsets.ModelViewSet):
    serializers_class = {
        "list": FollowToSerializer,
        "create": FollowCreateSerializer,
        "delete": FollowCreateSerializer,
        "update": FollowCreateSerializer,
        "follow_me":FollowMetListSerializer
    }
    # queryset = UserFollow.objects.all()

    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return UserFollow.objects.none()
        return UserFollow.objects.filter(follow_by=self.request.user)

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)

    @action(detail=False,methods=["get",])
    def follow_me(self, request, *args, **kwargs):
        queryset = UserFollow.objects.filter(follow_to=self.request.user)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
