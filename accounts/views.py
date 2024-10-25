from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from .forms import EmailAuthenticationForm


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = EmailAuthenticationForm  
    
class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')