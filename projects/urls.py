from . import views 
from django.urls import path

urlpatterns = [
    path('about/', views.about, name = 'about us'),
    path('', views.project, name = 'project'),
    path('single/<str:pk>/', views.singles, name = 'single'),
   
   ]