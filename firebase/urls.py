
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.Logar, name ='login'),
    path('cadastrar/',views.Cadastrar, name='cadastrar'),
    path('home/', views.Home, name='home')
  
    
    
    
   
]
