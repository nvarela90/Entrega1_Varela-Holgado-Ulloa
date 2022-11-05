from django.shortcuts import render, redirect
from datetime import datetime

from home.forms import JugadorFormulario, BusquedaJugadorFormulario

from home.models import Jugador

from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# def crear_jugador(request):
    
#     if request.method == 'POST':
        
#         formulario = JugadorFormulario(request.POST)
        
#         if formulario.is_valid():
#             data = formulario.cleaned_data
        
#             nombre = data['nombre']
#             apellido = data['apellido']
#             pais = data['pais']
#             edad = data['edad']
#             fecha_creacion = data['fecha_creacion'] or datetime.now()
            
#             jugador = Jugador(nombre=nombre, apellido=apellido, edad=edad, pais=pais, fecha_creacion=fecha_creacion)
#             jugador.save()
            
#             return redirect('ver-jugadores')
    
#     formulario = JugadorFormulario()
    
#     return render(request, 'home/crear_jugador.html', {'formulario': formulario})

#V2:
class CrearJugador(CreateView):
    model = Jugador
    success_url = '/jugadores/'
    template_name = 'home/crear_jugador.html'
    fields = ['nombre','apellido','pais','edad','fecha_creacion','descripcion']


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


class EditarJugador(UpdateView):
    model = Jugador
    success_url = '/jugadores/'
    fields = ['nombre', 'apellido', 'pais', 'edad', 'fecha_creacion','descripcion']
    template_name = 'home/editar_jugador.html'


class EliminarJugador(DeleteView):
    model = Jugador
    success_url = '/jugadores/'
    template_name = 'home/eliminar_jugador.html'


class VerJugador(DetailView):
    model = Jugador
    template_name = 'home/ver_el_jugador.html'