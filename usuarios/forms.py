from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class MiFormularioDeCreacion(UserCreationForm):
    
    first_name = forms.CharField(max_length=20, label='Nombre')
    last_name = forms.CharField(max_length=20, label='Apellido')
    email = forms.CharField() 
    password1 =forms.CharField(label = 'Contraseña', widget=forms.PasswordInput)
    password2 =forms.CharField(label = 'Repetir contraseña', widget=forms.PasswordInput)
      
    class Meta:
        
        model = User
        fields = ['username', 'first_name' , 'last_name', 'email','password1', 'password2']
        help_texts = {key: '' for key in fields}


class EditarPerfilUsuario(forms.Form):
    email = forms.CharField(label='e-mail')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')