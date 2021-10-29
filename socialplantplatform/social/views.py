from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser

from socialplantplatform.Base.BaseSerializers import SerializerNone
from socialplantplatform.social.Serializers.PublicationSerializers import PublicationListSerializer, PublicationCreateSerializer
from socialplantplatform.social.models import Publication


class PublicationViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    queryset = Publication.objects.all()
    serializers_class = {
        "list": PublicationListSerializer,
        "create":PublicationCreateSerializer,
        "retrieve":PublicationListSerializer,
        "update":PublicationCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)
