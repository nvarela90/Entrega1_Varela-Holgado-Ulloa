from django.urls import path
from mensajeria import views


urlpatterns = [
    
    path('mensajes/', views.ListaMensajes.as_view(), name = 'ver-mensajes'),
    path('mensajes/crear-mensaje/', views.CrearMensaje.as_view(), name = 'crear-mensaje'),
    path('mensajes/ver/<int:pk>', views.VerMensaje.as_view(), name= 'ver-mensaje'),

]   