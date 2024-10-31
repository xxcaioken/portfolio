from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback 
        fields = ['type', 'message']
        widgets = {
            'type': forms.Select(attrs={
                'class': 'form-control', 
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control', 
                'rows': 4,  
                'placeholder': 'Escreva seu feedback ou sugestão aqui...'
            }),
        }
