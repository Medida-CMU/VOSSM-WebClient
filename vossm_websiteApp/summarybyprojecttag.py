import pymongo
from pymongo import MongoClient
from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt
from django.http import *
import json 

database_name="VOSSM"
collection_name="raw_data"
collection_name_parse="parsed_data"

@csrf_exempt
def summary(request):
	data = {}
	count =1
	version = []
	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name_parse]
	dataCursor = collection.find()
	for record in dataCursor:
		record["_id"]["occurences"] = record["occurences"]
		data[count] = record["_id"]
		count = count+1

		print version

	print data
	return render(request, 'summarybyprojecttag.html', {"data" : data})

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
				data = get_graph_data(package_name);
		else:
			print 'why you do this!!'
    
	return HttpResponse(json.dumps(data), content_type = "application/json")

#{u'package': u'KernSmooth', u'start_time': u'Fri Dec 04 01:15:54 2015', u'system': u'Linux', u'hardware': u'x86_64', 
#u'version': u'2_23_14', u'end_time': u'Fri Dec 04 01:15:57 2015', u'_id': 1449283319.389087, u'user': u'9606278863337338470644244'}
def get_graph_data(package_name):
	data = {}
	system = {}
	hardware = {}
	version = {}
	user = {}
	connection = MongoClient()
	db = connection.VOSSM
	collection = db[collection_name]

	markersCursor = collection.find({'package' : package_name})

	for record in markersCursor:
		print record
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

		user[record['user']] = 1

	print len(user)
	print version
	print system
	print hardware

	data['system'] = system
	data['hardware'] = hardware
	data['version'] = version
	data['user'] = len(user)

	return data


