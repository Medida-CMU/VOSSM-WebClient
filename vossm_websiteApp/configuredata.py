import pymongo
from pymongo import MongoClient
#from pymongo import Connection
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
database_name="VOSSM"
collection_name="raw_data"
collection_name_parse="parsed_data"
@csrf_exempt
def configure(request):
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
 		data[count] = record["_id"]
		count = count+1

		print version

	print data
	return render(request, 'configuredata.html', {"data" : data})

@csrf_exempt
def update_config(request):
	checked_json = request.POST['checkedVal']
	unchecked_json = request.POST['uncheckedVal']
	checked_array = json.loads(checked_json)
	unchecked_array = json.loads(unchecked_json)
	print "----"
	print checked_array
	print unchecked_array
	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name_parse]
	for val in checked_array:
		collection.update( {"_id.package" : val}, {"$set" : {"selected": "true"} } )
	for val in unchecked_array:
		collection.update( {"_id.package" : val}, {"$set" : {"selected": "false"} } )
	print "updated"
	return HttpResponse({}, content_type = "application/json")
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