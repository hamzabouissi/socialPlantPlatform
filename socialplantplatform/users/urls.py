
from rest_framework.routers import DefaultRouter

from socialplantplatform.users.views import UsersViewSet

router = DefaultRouter()
router.register("users",UsersViewSet, basename="users")
app_name = "users"
urlpatterns = router.urls + [
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
