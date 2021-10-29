from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes

from socialplantplatform.Base.BaseSerializers import SerializerNone
from socialplantplatform.users.permissions import UserPermission
from socialplantplatform.users.serializers.UserSerializers import UserListSerializer, UserCreateSerializer

User = get_user_model()




class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    lookup_field = "username"
    serializers_class = {
        "list": UserListSerializer,
        "create": UserCreateSerializer,
        "retrieve": UserListSerializer,
        "update": UserCreateSerializer
    }
    permission_classes = (UserPermission,)

    def get_serializer_class(self):
        return self.serializers_class.get(self.action, SerializerNone)
# class UserDetailView(LoginRequiredMixin, DetailView):
#
#     model = User
#     slug_field = "username"
#     slug_url_kwarg = "username"
#
#
# user_detail_view = UserDetailView.as_view()
#
#
# class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
#
#     model = User
#     fields = ["name"]
#     success_message = _("Information successfully updated")
#
#     def get_success_url(self):
#         return self.request.user.get_absolute_url()  # type: ignore [union-attr]
#
#     def get_object(self):
#         return self.request.user
#
#
# user_update_view = UserUpdateView.as_view()
#
#
# class UserRedirectView(LoginRequiredMixin, RedirectView):
#
#     permanent = False
#
#     def get_redirect_url(self):
#         return reverse("users:detail", kwargs={"username": self.request.user.username})
#
#
# user_redirect_view = UserRedirectView.as_view()
