from django.shortcuts import render, redirect
from datetime import datetime

from home.forms import JugadorFormulario, BusquedaJugadorFormulario

from home.models import Jugador




def crear_jugador(request):
    
    if request.method == 'POST':
        
        formulario = JugadorFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            apellido = data['apellido']
            pais = data['pais']
            edad = data['edad']
            fecha_creacion = data['fecha_creacion'] or datetime.now()
            
            jugador = Jugador(nombre=nombre, apellido=apellido, edad=edad, pais=pais, fecha_creacion=fecha_creacion)
            jugador.save()
            
            return redirect('ver-jugadores')
    
    formulario = JugadorFormulario()
    
    return render(request, 'home/crear_jugador.html', {'formulario': formulario})




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


