from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control custom-input','placeholder':''}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control custom-input','placeholder':''}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control custom-input','placeholder':''}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control custom-input','placeholder':''}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']