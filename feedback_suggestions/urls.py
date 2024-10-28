from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback, name='feedback_suggestions'), 
    path('create_feedback/', views.create_feedback, name='create_feedback'),
]