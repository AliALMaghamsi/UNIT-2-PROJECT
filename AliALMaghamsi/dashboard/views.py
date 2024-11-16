from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from projects.models import Project
from main.models import Contact
# Create your views here.

def dashboard_view(request:HttpRequest,username, password):
            admin_name='Ali'
            admin_pass="Ali-123"
            
            if username==admin_name and password==admin_pass:    
                section = request.POST.get('section','projects')

                if section == 'projects':
                    if "search" in request.GET :
                        display= Project.objects.filter(title__contains=request.GET["search"])
                    elif "order_by" in request.GET and request.GET["order_by"]=="category":
                        display=Project.objects.filter().order_by("-category")
                    elif "order_by" in request.GET and request.GET["order_by"]=="completed_date":
                        display=Project.objects.filter().order_by("-completed_date")
                    else:
                        display = Project.objects.all()  
                      
                    
                elif section == 'messages':
                    display=Contact.objects.all()
                else:
                    display=None
                return render(request,"dashboard/dashboard.html",context={"section":section,"display":display,"user":admin_name,"password":admin_pass})
            else:
                 return redirect("dashboard:error_view")
            
       
            

def error_view(request:HttpRequest):
    return render(request,"dashboard/dasherror.html")