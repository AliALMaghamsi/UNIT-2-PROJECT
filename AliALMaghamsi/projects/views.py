from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from .models import Project
from .forms import ProjectForm



def all_projects_view(request:HttpRequest):
    projects = Project.objects.all()    
    return render(request,"projects/all_projects.html",context={'projects': projects})


def new_project_view(request:HttpRequest):
    project_form=ProjectForm()
    if request.method=='POST':
            project_form=ProjectForm(request.POST,request.FILES)
            if project_form.is_valid():
                project_form.save()
                return redirect('dashboard:dashboard_view',"Ali","Ali-123")
            else:
                project_form=ProjectForm()

    return render(request,'projects/new_project.html',context={'project_form':ProjectForm , 'category':Project.CategoryChoices.choices})


def project_detail_view(request:HttpRequest,project_id:int):
    try:
        project=Project.objects.get(pk=project_id)
        
    except Exception :
        return redirect('main:error_view')
    
    return render(request,'projects/project_detail.html',context={'project':project})


def update_project_view(request:HttpRequest,project_id:int):
    try:
        project=Project.objects.get(pk=project_id)
        if request.method=='POST':
            project=ProjectForm(request.POST,request.FILES,instance=project)
            if project.is_valid():
                project.save()
                return redirect('dashboard:dashboard_view',"Ali","Ali-123")
            else:
                redirect('projects:update_project_view',project.id)
    except Exception :
        return redirect('main:error_view')
    
    return render(request,'projects/update_project.html',context={'project':project,'category':project.CategoryChoices.choices})


def delete_project_view(request:HttpRequest,project_id:int):
    project=Project.objects.get(pk=project_id)
    project.delete()
    return redirect('dashboard:dashboard_view',"Ali","Ali-123")
