from django.urls import path
from home import views


urlpatterns = [
    
    path('', views.index, name= 'index'),
    path('jugadores/', views.ver_jugadores, name = 'ver-jugadores'),
    path('crear-jugador/', views.CrearJugador.as_view(), name = 'crear-jugador'),
    path('about/', views.about, name= 'about'),
    path('jugadores/editar/<int:pk>', views.EditarJugador.as_view(), name='editar_jugador'),
    path('jugadores/eliminar/<int:pk>', views.EliminarJugador.as_view(), name='eliminar_jugador'),
    path('jugadores/ver/<int:pk>', views.VerJugador.as_view(), name= 'ver_jugador'),

]    

