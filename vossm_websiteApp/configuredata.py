from django.shortcuts import render

def configure(request):
    
    return render(request, 'configuredata.html', {})