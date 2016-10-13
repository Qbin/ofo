from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def ofo(request):
    return render(request, 'ofo.html')
