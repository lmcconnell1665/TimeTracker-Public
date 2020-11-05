from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Setup custom user attributes for registration form
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    
    #defining that we want to save to the user database
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]