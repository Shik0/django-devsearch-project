from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

projectList = [
    {
        'id': '1',
        'title': 'Ecommerce website',
        'description': 'Ecommerce web site description'
    },
    {
        'id': '2',
        'title': 'Portfolio website',
        'description': 'Portfolio web site description'
    },
    {
        'id': '3',
        'title': 'Social network',
        'description': 'Desctiption of the project'
    }    
]

page = "projects"
number = 15
context = {"page": page, "number": number, "projects": projectList}

def projects(request):
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})