from django.db import models
from django.contrib.auth.models import User

class LinkedInProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relaciona o perfil do LinkedIn ao User
    linkedin_url = models.URLField(max_length=200, blank=True, null=True)  # Campo para armazenar o link do LinkedIn

    def __str__(self):
        return f"{self.user.username}'s LinkedIn Profile"