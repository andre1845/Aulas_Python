from django.shortcuts import render

# Create your views here.
# equacao/views.py

from django.http import JsonResponse
import math

def calcular_raizes(request):
    a = float(request.GET.get('a', 0))
    b = float(request.GET.get('b', 0))
    c = float(request.GET.get('c', 0))
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return JsonResponse({'erro': 'A equação não possui raízes reais.'})
    
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    raiz2 = (-b - math.sqrt(delta)) / (2 * a)
    
    return JsonResponse({'raiz1': raiz1, 'raiz2': raiz2})

def index(request):
    return render(request, 'equacao/index.html')
