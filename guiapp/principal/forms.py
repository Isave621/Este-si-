from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


class RegistroForm(UserCreationForm):

    class Meta:
        model = User 
        fields = [
                 'username',
                 'first_name',
                 'last_name',
                 'email',
        ]

class PerfilForm(forms.ModelForm):
     class Meta:
         model = Perfil
         fields =  ['nombre', 'direccion', 'imagen']