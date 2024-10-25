from django.urls import path
from .views import RegisterView, CustomLoginView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),  # Adiciona a rota de registro
]
