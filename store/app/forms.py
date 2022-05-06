from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import *
from django import forms

from django.contrib.auth.models import User

class LoginUserForm(AuthenticationForm):

    username = forms.CharField(
        label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))


class RegisterUserForm(UserCreationForm):

    username = forms.CharField(
        label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(
        label='email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='password repeat', widget=forms.PasswordInput(
        attrs={'class': 'form-input'}))

    class Meta:
        model = User 
        fields = ('username', 'email', 'password1', 'password2')

