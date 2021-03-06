from . import views
from django.urls import path

urlpatterns = [
    path('', views.project, name='project'),
    path('singleproject/<str:pk>/', views.singleproject, name='projects'),
    path('create-project/', views.createProject, name='create-project'),

    path('update-project/<str:pk>/', views.updateProject, name= 'update-project'),
    path('delete-project/<str:pk>/', views.deleteProject, name= 'delete-project'),
]
