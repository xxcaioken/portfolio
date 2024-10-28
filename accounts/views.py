from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import LinkedInProfile 
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.contrib.auth import login

class CustomLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('feedback_suggestions')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        return super().form_valid(form)

    def form_invalid(self, form):
        print("Formulário de login inválido! Erros:", form.errors)
        return super().form_invalid(form)



class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        
        if(user):
            LinkedInProfile.objects.create(user=user) 
        
        print("Formulário de registro válido! Dados:", form.cleaned_data)
        return super().form_valid(form)

    def form_invalid(self, form):
        print("Formulário de registro inválido! Erros:", form.errors)
        return super().form_invalid(form)