#from pymongo import Connection
import pymongo
from pymongo import MongoClient
from bson.json_util import dumps
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
import json, ast
from django.views.decorators.csrf import csrf_exempt
database_name="VOSSM"
collection_name_parse="parsed_data"
collection_raw = "raw_data"

def share(request):

    data = {}
    count =1
    version = []
    connection = MongoClient()
    db = connection.VOSSM
    collection = db[collection_name_parse]
    dataCursor = collection.find()
    for record in dataCursor:
        record["_id"]["occurences"] = record["occurences"]
        record["_id"]["selected"] = record["selected"]
        data[count] = ast.literal_eval(json.dumps(record["_id"]))
        count = count+1
    
    return render(request, 'share.html', {'data': data})

@csrf_exempt
def download_json(request):
    data = []
    checked_json = request.POST['checkedVal']
    checked_array = json.loads(checked_json)
    connection = MongoClient()
    db = connection.VOSSM
    collection = db[collection_raw]
    for val in checked_array:
        dataCursor = collection.find({"package" :{'$regex': val}})
        for record in dataCursor:
            data.append(record)
    return HttpResponse(json.dumps(data), content_type = "application/json")
