from pydoc import describe
from django.shortcuts import render

# Create your views here.
from unicodedata import name
from django.shortcuts import HttpResponse


def about(request):
    return render(request, 'about.html')


list_dict = [
    {
        'id': 1,
        'title': 'E-commerce project',
        'description': 'This is a full featured e-commerce website'
    },
    {
        'id' : 2,
        'title' : 'Blog Web',
        'description': 'This is public blogsite'
    },

    {
        'id': 3,
        'title': 'Python web',
        'description': 'This website for learning python'
    },

]


def project(request):
    msg = "You are in the project page"
    number = 10
    context = {'message': msg, 'Number': number, 'list_dict':list_dict}
    return render(request, 'project/projects.html', context)


def singles(request, pk):
    projectobj = None
    for i in list_dict:
        if i['id'] == pk:
            projectobj = i
    return render(request, 'project/single-project.html', {'singles': projectobj},)
