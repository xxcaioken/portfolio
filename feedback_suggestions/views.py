from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def feedback(request):
    screen_width = int(request.GET.get('screen_width', 0))
    screen_height = int(request.GET.get('screen_height', 0))
    print(f"Tamanho da tela: {screen_width}x{screen_height}")

    form = FeedbackForm()

    feedbacks = Feedback.objects.select_related('user__linkedinprofile').all().order_by('-date')
    
    maxPerPage = 3
    if screen_width < 426:
        maxPerPage = 1
    elif 426 <= screen_width < 1205:
        maxPerPage = 2

    feedback_batches = [feedbacks[i:i + maxPerPage] for i in range(0, len(feedbacks), maxPerPage)]
    
    return render(request, 'feedback_suggestions/index.html', {
        'feedback_batches': feedback_batches, 
        'form': form
    })


@login_required
def create_feedback(request):
    success_url = reverse_lazy('feedback')

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
    else:
        form = FeedbackForm() 
        
    return render(request, 'feedback_suggestions/create_feedback.html', {'form': form})
