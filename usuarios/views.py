from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from usuarios.forms import MiFormularioDeCreacion, EditarPerfilUsuario
from django.contrib.auth.decorators import login_required
from usuarios.models import ExtensionUsuario
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def iniciar_sesion(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.get_user()    
            login(request, usuario)
            return redirect('index')
    else:
        formulario = AuthenticationForm()
            
    return render(request, 'usuarios/iniciar_sesion.html', {'formulario':formulario})



def registrar(request):
    
    if request.method == 'POST':
        formulario= MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            
            return redirect('index')
    else:
        formulario= MiFormularioDeCreacion()    
    

    return render(request, 'usuarios/registrar.html', {'formulario':formulario})


@login_required
def perfil(request): 
    extensionUsuario, usuario_nuevo = ExtensionUsuario.objects.get_or_create(user = request.user)
    return render(request, 'usuarios/perfil.html',{})


@login_required
def editar_perfil(request):
    
    user = request.user
      
    if request.method == 'POST':
        formulario = EditarPerfilUsuario(request.POST, request.FILES)
        if formulario.is_valid():
            datos_nuevos = formulario.cleaned_data  
            user.first_name = datos_nuevos['first_name']
            user.last_name = datos_nuevos['last_name']
            user.email = datos_nuevos['email']
            user.extensionusuario.avatar = datos_nuevos['avatar']
            
            user.extensionusuario.save()
            user.save()
            
            return redirect('perfil')
            
    else:
        formulario = EditarPerfilUsuario(initial={
            'first_name':request.user.first_name,
            'last_name':request.user.last_name,
            'email':request.user.email,
            'avatar': user.extensionusuario.avatar,
            })
    
    return render(request, 'usuarios/editar-perfil.html',{'formulario':formulario})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = '/usuarios/perfil/'