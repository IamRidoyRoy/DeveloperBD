from pydoc import describe
from turtle import title
from django.shortcuts import render

# Create your views here.
from unicodedata import name
from django.shortcuts import HttpResponse
from .models import Project


def about(request):
    return render(request, 'about.html')


list_dict = [
    {
        'id': 1,
        'title': 'E-commerce project',
        'description': 'This is a full featured e-commerce website'
    },
    {
        'id': 2,
        'title': 'Blog Web',
        'description': 'This is public blogsite'
    },

    {
        'id': 3,
        'title': 'Python web',
        'description': 'This website for learning python'
    },


]


def project(request):
    allproject = Project.objects.all()
    context = {'allproject': allproject}
    return render(request, 'project/projects.html', context)


def singleproject(request, pk):
    projectobj = Project.objects.get(id=pk)
    # print('projectobj:', projectobj)
    return render(request, 'project/single-project.html', {
        'projectobj': projectobj,
    }, 
    )
