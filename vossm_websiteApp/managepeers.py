import pymongo
from pymongo import MongoClient
#from pymongo import Connection
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
database_name="vossmDB"
collection_name="Users"
@csrf_exempt
def manage(request):
    #connection = Connection()

    #db = connection[database_name]
    connection = MongoClient()
    db = connection.vossmDB
    collection = db[collection_name]

    data= {}
    
    cursor=collection.find();
    count=0
    for record in cursor:
        data[count]=record
        count=count+1
    print data
    
    return render(request, 'managepeers.html', {'data': data})