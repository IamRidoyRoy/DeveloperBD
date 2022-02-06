from . import views 
from django.urls import path

urlpatterns = [
    path('', views.project, name = 'project'),
    path('singleproject/<str:pk>/', views.singleproject, name = 'projects'),
   
   ]