from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import RecordCount


router =DefaultRouter()
router.trailing_slash = "/?"
urlpatterns = router.urls +[
    path(
        "record/count",
        RecordCount.as_view(),
        name = "record count"
    )


]