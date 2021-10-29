from rest_framework.routers import DefaultRouter

from socialplantplatform.plants.views import PlantsViewSet, UserPlantsViewSet

app_name = "plants"


router = DefaultRouter()
router.register("plants", PlantsViewSet, basename="plants")
router.register("user_plants", UserPlantsViewSet, basename="plants")
urlpatterns = router.urls
