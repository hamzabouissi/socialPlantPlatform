from django_filters import rest_framework as filters

from socialplantplatform.plants.models import User


class UserFilter(filters.FilterSet):

    class Meta:
        model = User
        fields = ("username","email")
