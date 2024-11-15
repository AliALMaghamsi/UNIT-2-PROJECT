from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from projects.models import Project
from main.models import Contact
# Create your views here.

def dashboard_view(request:HttpRequest):
    
        section = request.POST.get('section','projects')

        if section == 'projects':
            if "search" in request.GET :
                display= Project.objects.filter(title__contains=request.GET["search"])
            else:
                display = Project.objects.all()  
            
        elif section == 'messages':
            display=Contact.objects.all()
        else:
            display=None

        return render(request,"dashboard/dashboard.html",context={"section":section,"display":display})
