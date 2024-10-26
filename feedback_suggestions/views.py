from django.shortcuts import render
from .models import Feedback
from .forms import FeedbackForm

def feedback(request):
    form = FeedbackForm()
    feedbacks = Feedback.objects.all().order_by('-date')
    feedback_batches = [feedbacks[i:i+3] for i in range(0, len(feedbacks), 3)]
    return render(request, 'feedback_suggestions/index.html', {'feedback_batches': feedback_batches, 'form': form})
