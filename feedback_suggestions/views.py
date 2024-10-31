from django.shortcuts import render, redirect
from .models import Feedback
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import Http404

def feedback(request):
    screen_width = int(request.GET.get('screen_width', 0))
    screen_height = int(request.GET.get('screen_height', 0))
    print(f"Tamanho da tela: {screen_width}x{screen_height}")

    form = FeedbackForm()
    feedbacks = Feedback.objects.select_related('user__linkedinprofile').all().order_by('-date')
    
    maxPerPage = 4
    if screen_width < 425:
        maxPerPage = 1
    elif 425 <= screen_width < 1440:
        maxPerPage = 2
    elif 1440 <= screen_width < 2560:
        maxPerPage = 3
    else:
        maxPerPage = 4

    feedback_batches = [feedbacks[i:i + maxPerPage] for i in range(0, len(feedbacks), maxPerPage)]
    
    return render(request, 'feedback_suggestions/index.html', {
        'feedback_batches': feedback_batches, 
        'form': form
    })

@login_required
def create_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback_instance = form.save(commit=False)
            feedback_instance.user = request.user
            feedback_instance.save()
            return redirect('feedback_suggestions') 

        raise Http404("Formulário inválido")

    raise Http404("Método não permitido")
