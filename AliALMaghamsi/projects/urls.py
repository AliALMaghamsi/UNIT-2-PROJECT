from django.urls import path
from . import views


app_name='projects'

urlpatterns=[
    path('all/',views.all_projects_view,name='all_projects_view'),
]