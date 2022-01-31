from . import views 
from django.urls import path

urlpatterns = [
    path('', views.project, name = 'project'),
    path('projects/<str:pk>/', views.projects, name = 'projects'),
   
   ]