#from pymongo import Connection
import pymongo
from pymongo import MongoClient
from django.shortcuts import render

database_name="vossmDB"
collection_name="dummy"

def home(request):
    #connection = Connection()

    #db = connection[database_name]
    connection = MongoClient()
    db = connection.vossmDB
    collection = db[collection_name]

    data={}
    data['count']=collection.find().count();

    print data
    
    return render(request, 'home.html', {})