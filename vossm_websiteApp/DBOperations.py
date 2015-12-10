import pymongo
from pymongo import MongoClient
from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import *
import json 
from sets import Set
import re
import subprocess
from datetime import datetime

database_name = "VOSSM"
collection_name = "raw_data"
collection_name_parse = "parsed_data"
database_name_R_cran = "test"
collection_name_R_cran = "package_details"
collection_name_tag_list="tags"
collection_name_tag_mapping="tag_mapping"

@csrf_exempt
def DBOperation(request):
	c = {}
	c.update(csrf(request))

	markers = []
	plan_name = ''
	plan_desc = ''
	task_points = []
	data = []
	template_name = ''

	if request.is_ajax():
		if request.method == "POST":
			if request.POST['operation'] == 'getData':
				package_name = request.POST['packageName']
				data = get_graph_data(package_name)
			if request.POST['operation'] == 'getTagData':
				tag_name = request.POST['tagName']
				data = get_tag_data(tag_name)
			if request.POST['operation'] == 'getDataDate':
				start_date = request.POST['startDate']
				end_date = request.POST['endDate']
				data = get_date_data(start_date, end_date)
		else:
			print 'why you do this!!'
    
	return HttpResponse(json.dumps(data), content_type = "application/json")

def get_tag_data(tagName):
	data = {}
	system = {}
	hardware = {}
	version = {}
	user = {}
	arr = []

	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name_tag_mapping]
	collection_raw = db[collection_name]

	markersCursor = collection.find({'tags' : tagName})
	tag_package_list = []
	package_list = []
	raw_package_list = []
	for record in  markersCursor:
		tag_package_list.append(record['_id'])
	
	for tagDetail in tag_package_list:
		markersCursor = collection_raw.find({'package' : tagDetail['package'], 'system' : tagDetail['system'], 
			'version' : tagDetail['version'], 'hardware' : tagDetail['hardware'], 'language' : tagDetail['language']})

		'''getting raw detail about the packages'''
		for record in markersCursor:
			raw_package_list.append(record)
			if system.get(record['system']) != None:
				system[record['system']] = system.get(record['system']) + 1
			else:
				system[record['system']] = 1

			if hardware.get(record['hardware']) != None:
				hardware[record['hardware']] = hardware.get(record['hardware']) + 1
			else:
				hardware[record['hardware']] = 1

			if version.get(record['version']) != None:
				version[record['version']] = version.get(record['version']) + 1
			else:
				version[record['version']] = 1

			if user.get(record['user']) != None:
				user[record['user']] = user.get(record['user']) + 1
			else:
				user[record['user']] = 1
				
		data['system'] = system
		data['hardware'] = hardware
		data['version'] = version
		data['user'] = len(user)

	data['tag_package_list'] = tag_package_list
	# data['raw_package_list'] = raw_package_list
	return data

''' Get package data'''
def get_package_data(package_name):
	connection = MongoClient()
	db = connection.test
	collection = db[collection_name_R_cran]
	
	markersCursor = collection.find({'name' : package_name}, {'_id' : 0})
	
	for record in  markersCursor:
		return record

def get_unix_package_data(package_name):
	x=subprocess.check_output('apt-cache show '+ package_name, shell=True)
	print x
#{u'package': u'KernSmooth', u'start_time': u'Fri Dec 04 01:15:54 2015', u'system': u'Linux', u'hardware': u'x86_64', 
#u'version': u'2_23_14', u'end_time': u'Fri Dec 04 01:15:57 2015', u'_id': 1449283319.389087, u'user': u'9606278863337338470644244'}
def get_graph_data(package_name):
	data = {}
	system = {}
	hardware = {}
	version = {}
	user = {}
	arr = []
	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name]

	markersCursor = collection.find({'package' : package_name})
	language = ""
	for record in markersCursor:
		if system.get(record['system']) != None:
			system[record['system']] = system.get(record['system']) + 1
		else:
			system[record['system']] = 1

		if hardware.get(record['hardware']) != None:
			hardware[record['hardware']] = hardware.get(record['hardware']) + 1
		else:
			hardware[record['hardware']] = 1

		if version.get(record['version']) != None:
			version[record['version']] = version.get(record['version']) + 1
		else:
			version[record['version']] = 1

		if user.get(record['user']) != None:
			user[record['user']] = user.get(record['user']) + 1
		else:
			user[record['user']] = 1
		language = record['language']

	if language == "R":
		arr.append(get_package_data(package_name))
	if language == "Unix":
		arr.append(get_unix_package_data(package_name))

	data['detail'] = arr
	data['system'] = system
	data['hardware'] = hardware
	data['version'] = version
	data['user'] = len(user)

	return data

def get_date_data(start_date, end_date):
	data = {}
	system = {}
	hardware = {}
	version = {}
	user = {}
	system_duration = {}
	hardware_duration = {}
	arr = []

	start_date = datetime.strptime(start_date, '%m/%d/%Y')
	end_date = datetime.strptime(end_date, '%m/%d/%Y')

	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name]

	markersCursor = collection.find({'language' : 'R'}, {'_id':0})
	filteredRecords = []
	for record in markersCursor:
		date = record['start_time']
		date = datetime.strptime(date, '%c')
		if date >= start_date and date <=end_date:
			filteredRecords.append(record)
	
	listreducedRecord = []
	for record in filteredRecords:
		reducedRecord = {}
		if system.get(record['system']) != None:
			system[record['system']] = system.get(record['system']) + 1
			system_duration[record['system']] = system_duration.get(record['system']) + record['duration']
			
		else:
			system[record['system']] = 1
			system_duration[record['system']] = record['duration']

		if hardware.get(record['hardware']) != None:
			hardware[record['hardware']] = hardware.get(record['hardware']) + 1
			hardware_duration[record['hardware']] = hardware_duration.get(record['hardware']) + record['duration']
		else:
			hardware[record['hardware']] = 1
			hardware_duration[record['hardware']] = record['duration']

		if version.get(record['version']) != None:
			version[record['version']] = version.get(record['version']) + 1
		else:
			version[record['version']] = 1

		if user.get(record['user']) != None:
			user[record['user']] = user.get(record['user']) + 1
		else:
			user[record['user']] = 1
		reducedRecord['package'] = record['package']
		reducedRecord['hardware'] = record['hardware']
		reducedRecord['system'] = record['system']
		reducedRecord['version'] = record['version']
		reducedRecord['language'] = record['language']

		listreducedRecord.append(reducedRecord)

	seen = set()
	new_l = []
	for d in listreducedRecord:
	    t = tuple(d.items())
	    if t not in seen:
	        seen.add(t)
	        new_l.append(d)

	data['system'] = system
	data['hardware'] = hardware
	data['version'] = version
	data['user'] = len(user)
	data['system_duration'] = system_duration
	data['hardware_duration'] = hardware_duration

	data['tag_package_list'] = new_l

	return data