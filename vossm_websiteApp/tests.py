"""follow=True
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
import unittest
import mongoengine
from mongoengine import *
from django.test import Client
import json


class SimpleTest(unittest.TestCase):

	    # Stop ORM-related stuff from happening as we don't use the ORM
    
    def test_get_configure(self):
        '''
        Tests get data for configure data view
        '''
        c = Client()
        response=c.get('/configure/')
        status=200
        self.assertEquals(response.status_code,status)

    def test_update_operation(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        id=[{'package': 'survival', 'selected': 'true', 'system': 'Windows', 'hardware': 'x86_64', 'version': '2_37_7', 'occurences': 2}]
        #response=c.post('/update_config/',{'operation':['getData'],'tagList':['asdf,asdfsfdsfd'],'id':id},content_type="application/json")
        response=c.post('/update_config/',{'operation':'getData','tagList':['asdf,bcd'],'id':id})
        print response
        status=200
        self.assertEquals(response.status_code,status)

    def test_insert_operation(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        id=[{'package': 'survival', 'selected': 'true', 'system': 'Linux', 'hardware': 'x86_32', 'version': '2_37_7', 'occurences': 2}]
        #response=c.post('/update_config/',{'operation':['getData'],'tagList':['asdf,asdfsfdsfd'],'id':id},content_type="application/json")
        response=c.post('/update_config/',{'operation':'getData','tagList':['asdf,bcd'],'id':id})
        print response
        status=200
        self.assertEquals(response.status_code,status)

    def test_get_tagList_operation(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        response=c.post('/update_config/',{'operation':'getTagList'})
        status=200
        self.assertEquals(response.status_code,status)

    
    def test_update_config_operation(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        checkedVal = '["codetools","survival","splines","survival","codetools","parallel","compiler","KernSmooth","lattice","cluster","spatial","lattice","KernSmooth","splines","foreign","grid","nlme","mgcv","spatial","splines","tcltk","Matrix","cluster","class","boot","compiler","mgcv","rpart","nnet","tcltk","MASS","parallel","nnet","nlme","boot","stats4","grid","rpart","Matrix","MASS","stats4"]'
        uncheckedVal = '["class","foreign"]'
        response=c.post('/update_config/',{'operation':'update_config','checkedVal':checkedVal,'uncheckedVal':uncheckedVal})
        print response
        status=200
        self.assertEquals(response.status_code,status)

    def test_update_get_tag_data_1(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        id=[{'package': 'survival', 'selected': 'true', 'system': 'Windows', 'hardware': 'x86_64', 'version': '2_37_7', 'occurences': 2}]
        response=c.post('/update_config/',{'operation':'getTagData','id':id})
        status=200
        self.assertEquals(response.status_code,status)

    def test_update_get_tag_data_2(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        response=c.get('/sharedata/')
        status=200
        self.assertEquals(response.status_code,status)

    def test_update_get_tag_data_3(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        response=c.get('/sharedata/')
        status=200
        self.assertEquals(response.status_code,status)

    def test_get_package_data(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        response=c.post('/DBOperation/',{'operation':'getData','packageName':'parallel'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        status=200
        self.assertEquals(response.status_code,status)

    def test_get_package_data(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        response=c.post('/DBOperation/',{'operation':'getData','packageName':'splines'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        status=200
        self.assertEquals(response.status_code,status)

    def test_get_linux_package_data(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        response=c.post('/DBOperation/',{'operation':'getData','packageName':'python'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        status=200
        self.assertEquals(response.status_code,status)

    def test_get_tag_data(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        response=c.post('/DBOperation/',{'operation':'getTagData','tagName':'anandh'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        status=200
        self.assertEquals(response.status_code,status)

    def test_get_date_data(self):
        '''
        Tests update config method-getData operation
        '''
        c = Client()
        response=c.post('/DBOperation/',{'operation':'getDataDate','startDate':'12/02/2015','endDate':'12/05/2015'}, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        status=200
        self.assertEquals(response.status_code,status)