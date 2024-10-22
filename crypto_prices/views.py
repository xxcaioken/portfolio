from django.shortcuts import render

def crypto(request):
    return render(request, 'crypto_prices/index.html')
