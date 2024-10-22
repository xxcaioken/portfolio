from django.shortcuts import render

def feedback(request):
    return render(request, 'feedback_suggestions/index.html')
