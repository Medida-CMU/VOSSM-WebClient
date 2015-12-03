import pymongo
from pymongo import MongoClient
#from pymongo import Connection
from django.shortcuts import render

database_name="VOSSM"
collection_name="raw_data"

def configure(request):
	data = {}
	count =1
	version = []
	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name]
	dataCursor = collection.find()
	for record in dataCursor:
		data[count] = record
		count = count+1

		print version

	print data
	return render(request, 'configuredata.html', {"data" : data})

# def configure(request):
#     #connection = Connection()

#     #db = connection[database_name]
#     connection = MongoClient()
#     db = connection.vossmDB
#     collection = db[collection_name]

#     data={}
#     data['count']=collection.find().count();

#     print data
    
#     return render(request, 'configuredata.html', {})