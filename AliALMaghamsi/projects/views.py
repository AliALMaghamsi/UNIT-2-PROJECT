from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
# from .models import
# from .forms import



def all_projects_view(request:HttpRequest):
    return render(request,"projects/all_projects.html")
