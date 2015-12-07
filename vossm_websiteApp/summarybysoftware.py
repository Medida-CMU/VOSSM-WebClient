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

@csrf_exempt
def summary(request):
	data = {}
	count =1
	version = []
	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name_parse]
	dataCursor = collection.find()
	uniquePackage = set()

	for record in dataCursor:
		uniquePackage.add(record["_id"]["package"])

	count = 1
	mapTmp = {}
	for record in uniquePackage:
		mapTmp["package"] = record
		data[count] = mapTmp
		count = count+1
		mapTmp = {}
	return render(request, 'summarybysoftware.html', {"data" : data})

