from pymongo import Connection
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
    connection = Connection()

    db = connection[database_name]
    collection = db[collection_name]

    data= {}
    
    cursor=collection.find();
    count=0
    for record in cursor:
        data[count]=record
        count=count+1
    print 'Get method'
    print data
    
    
    return render(request, 'share.html', {'data': data})

@csrf_exempt
def filter(request):
    connection = Connection()
    db = connection[database_name]
    collection = db[collection_name]
    
    data={}
    response_array=[]
    if request.method == 'POST' and request.is_ajax():
        recieved_json_data=json.loads(request.raw_post_data)
        packageName=recieved_json_data['packageName']
        
    response_data={}
    cursor=collection.find({'PackageName':packageName});
    count=0
    for record in cursor:
        response_array.append(record)
        data[count]=record
        count=count+1
    #data['records']=response_array
    #result=data  
    print 'Filter:'
    print data
    #return HttpResponse(json.dumps(result),content_type="application/json")
    return render(request, 'share.html', {'data': data})        
    #return HttpResponse(json.dumps(response_data),content_type="application/json")
    #return render_to_response('share.html', c, RequestContext(request))