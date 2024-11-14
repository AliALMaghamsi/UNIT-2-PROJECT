from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from projects.models import Project
# Create your views here.

def dashboard_view(request:HttpRequest):
    
    
    
        section = request.POST.get('section','projects')

        if section == 'projects':
            display = Project.objects.all()  
            
        elif section == 'messages':
            display=None
        else:
            display=None

        return render(request,"dashboard/dashboard.html",context={"section":section,"display":display})
