rom django.shortcuts import render

def generate(request):
    
    return render(request, 'summarybysoftware.html', {})
