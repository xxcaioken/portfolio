# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()
        
class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

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
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')