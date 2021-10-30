from django.urls import path
from rest_framework.routers import DefaultRouter

from socialplantplatform.social.views import PublicationViewSet, FollowViewSet

app_name = "social"


router = DefaultRouter()
router.register("publications", PublicationViewSet, basename="publications")
router.register("follows", FollowViewSet, basename="follows")
urlpatterns = router.urls
