from .models import CommDisaster
from django.http import JsonResponse
from django.test import TestCase
from django.shortcuts import render
from data_resolver.views import read_json_data,import_json_data

import json

class ModelTest(TestCase):
			
# 数据库测试
	def test_can_insert_in_coomdisaster(self):
		disaster = CommDisaster()
		disaster.id = '0001112303'
		disaster.date = '2007-06-05 12:12:12'
		disaster.location = '530821102003'
		disaster.type='1'
		disaster.data= '23.132,102.307'
		disaster.structure='2'
		disaster.square='110'
		disaster.note=''
		disaster.reporting_unit='云南省人民政府办公厅' + '2'
		if disaster.pk is not None:
			disaster.delete()
		self.assertIsNone(disaster.pk)
		disaster.save()
		self.assertIsNotNone(disaster.pk)
		if disaster.pk is not None:
			disaster.delete()
		return

# 测试json输入
	def test_import_json_data(self):
		#用字典的格式存储测试的输入的json数据
		test_disaster = {
			"results": [
				{
					"id": "0001112223",
					"date": "20200505121212",
					"location": "000111000222223",
					"type": "123",
					"grade": "8",
					"picture": "100110000",
					"note": "12e2345ui765",
					"reporting_unit": "23562135"
				},
				{
					"id": "1001112223",
					"date": "20200504221212",
					"location": "111111000222223",
					"type": "111",
					"grade": "8",
					"picture": "1000001001",
					"note": "12e2345ui765",
					"reporting_unit": "2357654135"
				}
			]
		}
		url = "data_resolver/CommDisaster.json"
		import_json_data(url,test_disaster)


# 测试json输出
	def test_read_json_data(self):
		url = 'data_resolver/CommDisaster.json'
		read_json_data(url)

