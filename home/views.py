from django.shortcuts import render, redirect
from datetime import datetime

from home.forms import JugadorFormulario, BusquedaJugadorFormulario

from home.models import Jugador

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


class CrearJugador(LoginRequiredMixin, CreateView):
    model = Jugador
    success_url = '/jugadores/'
    template_name = 'home/crear_jugador.html'
    fields = ['nombre','apellido','pais','edad','fecha_creacion','descripcion', 'autor', 'imagen']


def ver_jugadores(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        jugadores = Jugador.objects.filter(nombre__icontains=nombre)
    else:
        jugadores = Jugador.objects.all()
    
    formulario = BusquedaJugadorFormulario()
    
    return render(request, 'home/ver_jugadores.html', {'jugadores': jugadores, 'formulario': formulario})


def about(request):
    
    return render(request, 'home/about.html')
  

def index(request):
    
    return render(request, 'home/index.html')


class EditarJugador(LoginRequiredMixin, UpdateView):
    model = Jugador
    success_url = '/jugadores/'
    fields = ['nombre', 'apellido', 'pais', 'edad', 'fecha_creacion','descripcion']
    template_name = 'home/editar_jugador.html'


class EliminarJugador(LoginRequiredMixin, DeleteView):
    model = Jugador
    success_url = '/jugadores/'
    template_name = 'home/eliminar_jugador.html'


class VerJugador(DetailView):
    model = Jugador
    template_name = 'home/ver_jugador.html'