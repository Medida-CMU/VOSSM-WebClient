import pymongo
from pymongo import MongoClient
#from pymongo import Connection
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json, ast

database_name="VOSSM"
collection_name="raw_data"
collection_name_parse="parsed_data"
collection_name_tag_list="tags"
collection_name_tag_mapping="tag_mapping"

def home(request):
	data = {}
	user = {}
	pkges = {}
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
	
	collection = db[collection_name]
	pkgCount = collection.find().count()
	dataCursor = collection.find()
	
	for record in dataCursor:
		if user.get(record['user']) != None:
			user[record['user']] = user.get(record['user']) + 1
		else:
			user[record['user']] = 1	

		if pkges.get(record['package']) != None:
			pkges[record['package']] = pkges.get(record['package']) + 1
		else:
			pkges[record['package']] = 1	

	data['pkgCount'] = pkgCount
	data['usrCount'] = len(user)
	data['pkges'] = pkges
	return render(request, 'home.html', {"data" : data})