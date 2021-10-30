from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from rest_framework.parsers import MultiPartParser

from socialplantplatform.Base.BaseSerializers import SerializerNone
from socialplantplatform.users.filters import UserFilter
from socialplantplatform.users.permissions import UserPermission
from socialplantplatform.users.serializers.UserSerializers import UserListSerializer, UserCreateSerializer

User = get_user_model()




class UsersViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    queryset = User.objects.all()
    lookup_field = "username"
    serializers_class = {
        "list": UserListSerializer,
        "create": UserCreateSerializer,
        "retrieve": UserListSerializer,
        "update": UserCreateSerializer
    }
    permission_classes = (UserPermission,)
    filterset_class = UserFilter

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)

