from django.shortcuts import render

# Create your views here.
from unicodedata import name
from django.shortcuts import HttpResponse
def about(request):
    return render(request, 'about.html')

def project(request):
    return render(request, 'project/projects.html')




def single_project(request):
     return render(request, 'project/single-project.html')