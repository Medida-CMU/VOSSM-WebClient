from django.shortcuts import render
from models import Employee


def index(request):
    
    return render(request, 'index.html', {})
