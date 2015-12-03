import pymongo
from pymongo import MongoClient
from django.shortcuts import render

def summary(request):
    
    return render(request, 'summarybyprojecttag.html', {})

