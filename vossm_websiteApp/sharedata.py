#from pymongo import Connection
import pymongo
from pymongo import MongoClient
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.template import Context, RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from datetime import datetime
from django.contrib.auth.models import User
import json 
import time
from datetime import datetime

database_name="vossmDB"
collection_name="Data"

def share(request):

    connection = MongoClient()
    db = connection.vossmDB
    collection = db[collection_name]

    data= {}
    
    cursor=collection.find();
    count=0
    for record in cursor:
        data[count]=record
        count=count+1
    
    
    return render(request, 'share.html', {'data': data})
