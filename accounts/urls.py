from django.urls import path
from .views import RegisterView, CustomLoginView, logout_view

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),
    
]
