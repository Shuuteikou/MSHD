from data_resolver.models import DeathStatics,CivilStructure,CommDisaster
from data_resolver.models import CollapseRecord,DisatserPrediction,DisasterRequest

from django.http import JsonResponse
from django.test import TestCase
from django.shortcuts import render
from data_resolver.views import read_json_data,import_json_data,id_mapping

import json

class ModelTest(TestCase):
			
# 数据库测试

	#DeathStatics
	def test_can_insert_in_DeathStatics(self):
		d_statics = DeathStatics()
		d_statics.id = '0101010020041111101'
		d_statics.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		d_statics.date = '2020-05-20 12:12:12'
		d_statics.number = '200'
		d_statics.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if d_statics.pk is not None:
			d_statics.delete()
		self.assertIsNone(d_statics.pk)
		d_statics.save()
		self.assertIsNotNone(d_statics.pk)
		if d_statics.pk is not None:
			d_statics.delete()
		return


	#CivilStructure
	def test_can_insert_in_CivilStructure(self):
		c_structure = CivilStructure()
		c_structure.id = '0101010020042211101'
		c_structure.date = '2020-05-20 12:12:12'
		c_structure.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		c_structure.basically_intact_square = '3000'
		c_structure.damaged_square = '1250'
		c_structure.destroyed_square = '1200'
		c_structure.note = '破坏情况比较严重'
		c_structure.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if c_structure.pk is not None:
			c_structure.delete()
		self.assertIsNone(c_structure.pk)
		c_structure.save()
		self.assertIsNotNone(c_structure.pk)
		if c_structure.pk is not None:
			c_structure.delete()
		return

	#CommDisaster
	def test_can_insert_in_CoomDisaster(self):
		disaster = CommDisaster()
		disaster.id = '0101010020043362202'
		disaster.date = '2007-06-05 12:12:12'
		disaster.location = '530821102003'
		disaster.type = '1'
		disaster.data = '23.132,102.307'
		disaster.structure = '2'
		disaster.square = '110'
		disaster.note = '较为严重'
		disaster.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if disaster.pk is not None:
			disaster.delete()
		self.assertIsNone(disaster.pk)
		disaster.save()
		self.assertIsNotNone(disaster.pk)
		if disaster.pk is not None:
			disaster.delete()
		return

	#CollapseRecord
	def test_can_insert_in_CollapseRecord(self):
		c_record = CollapseRecord()
		c_record.id = '0101010020044412202'
		c_record.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		c_record.date = '2020-05-20 12:12:12'
		c_record.type = '2'
		c_record.status = '2'
		c_record.note = '较为严重'
		# c_record.picture = cv2.imread('earthquake.jpg')
		c_record.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if c_record.pk is not None:
			c_record.delete()
		self.assertIsNone(c_record.pk)
		c_record.save()
		self.assertIsNotNone(c_record.pk)
		if c_record.pk is not None:
			c_record.delete()
		return

	#DisasterPrediction
	def test_can_insert_DisasterPrediction(self):
		d_prediction = DisatserPrediction()
		d_prediction.id = '0101010020044412202'
		d_prediction.date = '2020-05-20 12:12:12'
		d_prediction.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		d_prediction.longtitude = '118.80'
		d_prediction.latitude = '32.05'
		d_prediction.depth = '32.45'
		d_prediction.magnitude = '4.6'
		d_prediction.intensity = '6'
		d_prediction.type = '1'
		d_prediction.note = '受灾严重'
		# d_prediction.picture = '0000'
		d_prediction.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if d_prediction.pk is not None:
			d_prediction.delete()
		self.assertIsNone(d_prediction.pk)
		d_prediction.save()
		self.assertIsNotNone(d_prediction.pk)
		if d_prediction.pk is not None:
			d_prediction.delete()
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


#测试灾情编码
	def test_disaster_code(self):
		id_mapping(get_value = '0101010020041111101')

#测试将编码后识别的结果分别存入相应的数据表中

