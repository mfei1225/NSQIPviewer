from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import RecordCount,ColumnsNames,ColumnsDetails,ColumnsDetailsSingle


router =DefaultRouter()
router.trailing_slash = "/?"
urlpatterns = router.urls +[
    path(
        "record/count",
        RecordCount.as_view(),
        name = "record count"
    ),
    path(
        "columns",
        ColumnsNames.as_view(),
        name = "column names"
    )
    ,
    path(
        "columns/details",
        ColumnsDetails.as_view(),
        name = "column names"
    ),
     path(
        "columns/single/<str:filter>",
        ColumnsDetailsSingle.as_view(),
        name = "single column names"
    )



]