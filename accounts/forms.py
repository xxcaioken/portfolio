from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
import re

User = get_user_model()
        
class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        try:
            user = User.objects.get(email=email)
            if not user.check_password(password):
                raise forms.ValidationError("Credenciais inválidas.")
        except User.DoesNotExist:
            raise forms.ValidationError("Credenciais inválidas.")

        self.user_cache = user
        return cleaned_data

    def get_user(self):
        return self.user_cache
    
    

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    linkedin_url = forms.URLField(
        label='LinkedIn Profile URL',
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://www.linkedin.com/in/username', 'type': 'url'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'linkedin_url']  

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username:
            username = username.replace(' ', '_')
        return username
