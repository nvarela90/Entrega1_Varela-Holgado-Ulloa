from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    path('iniciar-sesion/', views.iniciar_sesion, name='iniciar-sesion'),
    path('registrar/', views.registrar, name='registrar'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='usuarios/cerrar_sesion.html' ), name='cerrar-sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar', views.editar_perfil, name='editar-perfil'),
    path('perfil/cambiar-contrasenia/', views.CambiarContrasenia.as_view(), name='cambiar-contrasenia'),
]
  