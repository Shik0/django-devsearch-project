from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm




def projects(request):
    projectList = Project.objects.all()
    context = {"projects": projectList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    context = {'project': projectObj}
    return render(request, 'projects/single_project.html', context)

def createProject(request):
    form = ProjectForm()
    context = {'form': form}
    return render(request, 'projects/project_form.html', context)