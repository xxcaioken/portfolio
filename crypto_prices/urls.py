from django.urls import path
from . import views

urlpatterns = [
    path('', views.crypto, name='crypto_prices'),
]
