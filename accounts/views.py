from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import LinkedInProfile
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect


class CustomLoginView(LoginView):
    form_class = EmailAuthenticationForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('feedback_suggestions')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        
        if user:
            linkedin_profile, _ = LinkedInProfile.objects.get_or_create(user=user)

            linkedin_url = form.cleaned_data.get('linkedin_url')
            if linkedin_url:
                linkedin_profile.linkedin_url = linkedin_url
                linkedin_profile.save()

        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

def logout_view(request):
    logout(request)
    return redirect('home')
