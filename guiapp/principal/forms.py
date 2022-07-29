from pyexpat import model
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *


#Registro de usuario
class RegistroForm(UserCreationForm):

    class Meta:
        model = User 
        fields = [
                 'username',
                 'first_name',
                 'last_name',
                 'email',
        ]


