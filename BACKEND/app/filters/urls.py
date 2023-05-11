from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import RecordCount,ColumnsNames,ColumnsDetails,FilterView,FilterExportView,Populate,TestNull,AddNull


router =DefaultRouter()
router.trailing_slash="/?"
router.register(r'columns/details', ColumnsDetails, basename="colmun details")
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
    ),
    path(
        "filter",
        FilterView.as_view(), 
        name = "filter"
    ),
    path(
        "filter/export",
        FilterExportView.as_view(), 
        name = "filter"
    )
    ,
    path(
        "populate",
        Populate.as_view(), 
        name = "fill_table"
    ),
    path(
        "addNull",
        AddNull.as_view(), 
        name = "fill_table"
    ),
    path(
        "null",
        TestNull.as_view(), 
        name = "fill_table"
    )

    ##Grace New Endpoint Insert Here. columns/all
    ##hello michael


]