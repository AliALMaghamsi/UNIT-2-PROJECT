from django.urls import path
from . import views


app_name='dashboard'

urlpatterns=[
    path("dashboard/<str:username>/<str:password>/",views.dashboard_view,name="dashboard_view"),
    path("error/",views.error_view,name="error_view")
     
]