from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, widgets




class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'style':'max-height: 1em','autofocus':'true'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style':'max-height: 1em'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','style':'max-height: 1em'}))

    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1', 'password2')
        widgets = {
            'password1':forms.PasswordInput(attrs={'class':'form-control','style':'max-height: 1em'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control','style':'max-height: 1em'}),
            'username':forms.TextInput(attrs={'class':'form-control','style':'max-height: 1em'}),     
        }
