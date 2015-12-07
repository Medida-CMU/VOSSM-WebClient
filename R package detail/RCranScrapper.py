from bs4 import BeautifulSoup
import urllib2
import pymongo
from pymongo import MongoClient

def get_name_company(packageName):

	package_page = urllib2.urlopen("https://cran.r-project.org/web/packages/"+ packageName +"/index.html")
	package_data = BeautifulSoup(package_page.read())

	package_record = {}

	package_record["name"] = packageName		
	for data in package_data.findAll("p"):
		package_record["description"] = data.get_text()

	previous = ""
	for data in package_data.findAll("table"):
		for comp in data.findAll("td"):
			if previous == "Version:":
				package_record["version"] = comp.get_text()
			
			if previous == "Depends:":
				package_record["depends"] = comp.get_text()
			
			if previous == "Published:":
				package_record["published"] = comp.get_text()

			if previous == "Author:":
				package_record["author"] = comp.get_text()

			if previous == "Maintainer:":
				package_record["maintainer"] = comp.get_text()

			if previous == "License:":
				package_record["license"] = comp.get_text()

			previous = comp.get_text()

	print package_record
	return package_record

database_name="VOSSM"
collection_name="R_cran_data"

connection = MongoClient()
db = connection.VOSSM
collection = db[collection_name]
collection.insert(get_name_company("spatial"))
collection.insert(get_name_company("foreign"))