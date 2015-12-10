import pymongo
from pymongo import MongoClient
from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import *
import json 
from sets import Set

database_name = "VOSSM"
collection_name = "raw_data"
collection_name_parse = "parsed_data"
database_name_R_cran = "test"
collection_name_R_cran = "package_details"
collection_name_tag_list="tags"
collection_name_tag_mapping="tag_mapping"

@csrf_exempt
def summary(request):
	data = {}
	count = 0
	version = []
	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name_tag_list]
	dataCursor = collection.find()

	count = 1
	for record in dataCursor:
		data[count] = record
		count+= 1

	return render(request, 'summarybyday.html', {"data" : data})