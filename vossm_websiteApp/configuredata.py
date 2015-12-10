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
 		data[count] = ast.literal_eval(json.dumps(record["_id"]))
		count = count+1
	
	return render(request, 'configuredata.html', {"data" : data})

@csrf_exempt
def update_config(request):
	
	if request.POST['operation'] == 'getData':
		print request.POST
		tag_list = request.POST['tagList']
		idField = request.POST['id']
		idField = idField.replace("'", "\"");
		val = json.loads(idField)
		val.pop("selected")
		val.pop("occurences")
		
		connection = MongoClient()
		db = connection.VOSSM
		collection = db[collection_name_tag_mapping]
		tags_collection = db[collection_name_tag_list]
		
		'''add tag to the tag Database'''
		tagsArr = tag_list.split(',')

		for tag in tagsArr:
			if tags_collection.find({"tag" : tag}).count() == 0:
				tags_collection.insert({"tag" : tag})
		'''add tag to the tag Database'''
		
		recordCount = collection.find({"_id" : val}).count()
		
		if recordCount > 0:
			collection.update( {"_id" : val}, {"$set" : {"tags": tagsArr} } )
		else:
			collection.insert({"_id" : val, "tags" : tagsArr})
	

	''' retrieve and return all tags '''
	if request.POST['operation'] == 'getTagList':
		data = []
		connection = MongoClient()
		db = connection.VOSSM
		tags_collection = db[collection_name_tag_list]
		
		'''add tag to the tag Database'''
		markersCursor = tags_collection.find({})

		for record in markersCursor:
			data.append(record['tag'])
	
		return HttpResponse(json.dumps(data), content_type = "application/json")

	''' retrieve tag information of a single record'''
	if request.POST['operation'] == 'getTagData':
		data = {}
		tagCsv = ""
		idField = request.POST['id']
		idField = idField.replace("'", "\"");
		val = json.loads(idField)
		val.pop("selected")
		val.pop("occurences")

		connection = MongoClient()
		db = connection.VOSSM
		collection = db[collection_name_tag_mapping]
		markersCursor = collection.find({"_id" : val})
		for record in markersCursor:
			data = record['tags']

		'''convert array to csv'''
		for val in data:
			tagCsv+= val + ","

		data = tagCsv
		return HttpResponse(json.dumps(data), content_type = "application/json")

	if request.POST['operation'] == 'update_config':
		checked_json = request.POST['checkedVal']
		unchecked_json = request.POST['uncheckedVal']
		checked_array = json.loads(checked_json)
		unchecked_array = json.loads(unchecked_json)

		connection = MongoClient()
		db = connection.VOSSM
		collection = db[collection_name_parse]
		for val in checked_array:
			collection.update( {"_id.package" : val}, {"$set" : {"selected": "true"} } )
		for val in unchecked_array:
			collection.update( {"_id.package" : val}, {"$set" : {"selected": "false"} } )
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