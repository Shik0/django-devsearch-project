from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Project

# projectList = [
#     {
#         'id': '1',
#         'title': 'Ecommerce website',
#         'description': 'Ecommerce web site description'
#     },
#     {
#         'id': '2',
#         'title': 'Portfolio website',
#         'description': 'Portfolio web site description'
#     },
#     {
#         'id': '3',
#         'title': 'Social network',
#         'description': 'Desctiption of the project'
#     }    
# ]

# page = "projects"
# number = 15


def projects(request):
    projectList = Project.objects.all()
    context = {"projects": projectList}
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = Project.objects.get(id = pk)
    # for i in projectList:
    #     if i['id'] == pk:
    #         projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})