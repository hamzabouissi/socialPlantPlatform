from django_filters import rest_framework as filters

from socialplantplatform.social.models import Publication


class PublicationFilter(filters.FilterSet):
    class Meta:
        model = Publication
        fields = ("user__username", "story", "sell", "quantity",)
