from django.urls import path
from home import views

urlpatterns = [
    
    path('', views.index, name= 'index'),
    path('ver-jugadores/', views.ver_jugadores, name = 'ver-jugadores'),
    path('crear-jugador/', views.crear_jugador, name = 'crear-jugador'),
    path('about/', views.about, name= 'about')
    
 
 
 
    
]    
