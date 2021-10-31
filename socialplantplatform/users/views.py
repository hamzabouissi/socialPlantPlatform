from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import permission_classes, action
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from socialplantplatform.Base.BaseSerializers import SerializerNone
from socialplantplatform.users.filters import UserFilter
from socialplantplatform.users.permissions import UserPermission
from socialplantplatform.users.serializers.UserSerializers import UserListSerializer, UserCreateSerializer, \
    LoginSerializer, ProfileSerializer

User = get_user_model()


class UsersViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    queryset = User.objects.all()
    serializers_class = {
        "list": UserListSerializer,
        "create": UserCreateSerializer,
        "retrieve": UserListSerializer,
        "update": UserCreateSerializer,
        "login": LoginSerializer
    }
    permission_classes = (UserPermission,)
    filterset_class = UserFilter

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: UserListSerializer}
    )
    @action(detail=False, methods=["Post"], permission_classes=(AllowAny,),filterset_class=None)
    def login(self, request):
        ser = LoginSerializer(data=request.data)
        ser.is_valid(raise_exception=True)
        user = User.objects.get(username=ser.data['username'])
        return Response(UserListSerializer(user).data)

    @swagger_auto_schema(
        responses={status.HTTP_200_OK: ProfileSerializer}
    )
    @action(detail=False, methods=["Get"], permission_classes=(IsAuthenticated,),filterset_class=None)
    def my_profile(self, request):
        data = User.objects.profile_aggregate(request.user.id)
        ser = ProfileSerializer(data)
        return Response(ser.data)
