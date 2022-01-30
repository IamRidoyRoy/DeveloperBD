from . import views 
from django.urls import path

urlpatterns = [
    path('about/', views.about, name = 'about us'),
    path('', views.project, name = 'project'),
    path('single-project/', views.single_project, name = 'projects'),
   
   ]