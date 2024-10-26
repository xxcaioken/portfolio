from django.db import models
from django.contrib.auth.models import User  

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    type = models.CharField(max_length=50) 
    message = models.TextField()
    date = models.DateField(auto_now_add=True)  
    
    class Meta:
        unique_together = ('user', 'message', 'date') 

    def __str__(self):
        return f"{self.user.username} - {self.type}"
