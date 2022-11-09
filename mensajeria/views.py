from mensajeria.models import Mensaje
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin



class CrearMensaje(LoginRequiredMixin, CreateView):
    model = Mensaje
    success_url = '/mensajeria/mensajes'
    template_name = 'mensajeria/crear_mensaje.html'
    fields = ['texto', 'emisor', 'receptor']

class ListaMensajes(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'mensajeria/ver_mensajes.html'

class VerMensaje(DetailView):
    model = Mensaje
    template_name = 'mensajeria/ver_mensaje.html'




