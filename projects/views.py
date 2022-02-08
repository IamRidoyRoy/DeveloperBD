from multiprocessing import context
from pydoc import describe
from turtle import title
from django.shortcuts import redirect, render
# Create your views here.
from unicodedata import name
from django.shortcuts import HttpResponse
from .models import Project
from .forms import ProjectForm


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

def createProject(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('project')
    context = {'form': form}
    return render(request, "project/project_form.html", context)

def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project')
    context = {'form': form}
    return render(request, "project/project_form.html", context) 

