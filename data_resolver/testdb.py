from django.test import TestCase
from django.utils import unittest

from data_resolver.models import DeathStatics, MissingStatics, CivilStructure
from data_resolver.models import MasonryStructure, CommDisaster, TrafficDisaster
from data_resolver.midels import CollapseRecord, LandslideRecord, DisasterInfo
from data_resolver.models import DisatserPrediction,  DisasterRequest

class ModelTest(TestCase):

	#根据灾情信息的大类和子类编码，确定数据存入的数据表
	def test_disaster_type_choose (self):
		fake_id = '0101010020041111101' #此处应当从前端传来的json文件中获取真实的id
		disastertype_num = fake_id[12:15]
		if disastertype_num == '111':
			test_can_insert_in_DeathStatics(self)
		elif disastertype_num == '113':
			test_can_insert_in_MissingStatics(self)
		elif disastertype_num == '221':
			test_can_insert_in_CivilStructure(self)
		elif disastertype_num == '223':
			test_can_insert_in_MasonryStructure(self)
		elif disastertype_num == '331':
			test_can_insert_in_TrafficDisaster(self)
		elif disastertype_num == '336':
			test_can_insert_in_CommDisaster(self)
		elif disastertype_num == '441':
			test_can_insert_in_CollapseRecord(self)
		elif disastertype_num == '442':
			test_can_insert_in_LandslideRecord(self)
		elif disastertype_num == '551':
			test_can_insert_in_DisasterInfo(self)
		elif disastertype_num == '552':
			test_can_insert_DisasterPrediction(self)


#数据库测试

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

	#MissingStatics
	def test_can_insert_in_MissingStatics(self):
		m_statics = MissingStatics()
		m_statics.id = '0101010020041131101'
		m_statics.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		m_statics.date = '2020-05-20 12:12:12'
		m_statics.number = '30'
		m_statics.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if m_statics.pk is not None:
			m_statics.delete()
		self.assertIsNone(m_statics.pk)
		m_statics.save()
		self.assertIsNotNone(m_statics.pk)
		if m_statics.pk is not None:
			m_statics.delete()
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

	#MasonryStructure
	def test_can_insert_in_MasonryStructure(self):
		m_structure = MasonryStructure()
		m_structure.id = '0101010020042231101'
		m_structure.date = '2020-05-20 12:12:12'
		m_structure.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		m_structure.basically_intact_square = '3000'
		m_structure.slight_damaged_square = '300'
		m_structure.moderate_damaged_square = '300'
		m_structure.serious_damaged_square = '300'
		m_structure.destroyed_square = '400'
		m_structure.note = '破坏情况比较严重'
		m_structure.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if m_structure.pk is not None:
			m_structure.delete()
		self.assertIsNone(m_structure.pk)
		m_structure.save()
		self.assertIsNotNone(m_structure.pk)
		if m_structure.pk is not None:
			m_structure.delete()
		return 

	#CommDisaster
	def test_can_insert_in_CommDisaster(self):
		c_disaster = CommDisaster()
		c_disaster.id = '0101010020043362202'
		c_disaster.date = '2007-06-05 12:12:12'
		c_disaster.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		c_disaster.type = '1'
		c_disaster.data = '23.132,102.307'
		c_disaster.structure = '2'
		c_disaster.square = '110'
		c_disaster.note = '较为严重'
		c_disaster.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if c_disaster.pk is not None:
			c_disaster.delete()
		self.assertIsNone(c_disaster.pk)
		c_disaster.save()
		self.assertIsNotNone(c_disaster.pk)
		if c_disaster.pk is not None:
			c_disaster.delete()
		return


	#TrafficDisaster
	def test_can_insert_in_TrafficDisaster(self):
		t_disaster = TrafficDisaster()
		t_disaster.id = '0101010020043312202'
		t_disaster.date = '2007-06-05 12:12:12'
		t_disaster.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		t_disaster.type = '1'
		t_disaster.grade = '2'
		# t_disaster.picture = NULL 
		t_disaster.note = '严重'
		t_disaster.reporting_unit = '2202' + '江苏省人民政府办公厅'
		f t_disaster.pk is not None:
			t_disaster.delete()
		self.assertIsNone(t_disaster.pk)
		t_disaster.save()
		self.assertIsNotNone(t_disaster.pk)
		if t_disaster.pk is not None:
			t_disaster.delete()
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
		# c_record.picture = NULL
		c_record.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if c_record.pk is not None:
			c_record.delete()
		self.assertIsNone(c_record.pk)
		c_record.save()
		self.assertIsNotNone(c_record.pk)
		if c_record.pk is not None:
			c_record.delete()
		return

	#LandslideRecord
	def test_can_insert_in_LandslideRecord(self):
		l_record = LandslideRecord()
		l_record.id = '0101010020044412202'
		l_record.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		l_record.date = '2020-05-20 12:12:12'
		l_record.type = '2'
		l_record.status = '2'
		l_record.note = '较为严重'
		# l_record.picture = NULL
		l_record.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if l_record.pk is not None:
			l_record.delete()
		self.assertIsNone(l_record.pk)
		l_record.save()
		self.assertIsNotNone(l_record.pk)
		if l_record.pk is not None:
			l_record.delete()
		return

	#DisasterInfo
	def test_can_insert_in_DisasterInfo(self):
		d_info = DisasterInfo()
		d_info.id = '0101010020044412202'
		d_info.date = '2020-05-20 12:12:12'
		d_info.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		d_info.longtitude = '118.80'
		d_info.latitude = '32.45'
		d_info.depth = '32.45'
		d_info.magnitude = '6'
		# d_info.picture = NULL
		d_info.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if d_infp.pk is not None:
			d_info.delete()
		self.assertIsNone(d_info.pk)
		d_info.save()
		self.assertIsNotNone(d_info.pk)
		if d_info.pk is not None:
			d_info.delete()
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

	#DisasterRequest
	def test_can_insert_in_DisasterRequest(self):
		d_request = DisasterRequest()
		d_request.id = '0101010020044412202'
		d_request.date = '2020-05-20 12:12:12'
		d_request.disasterType = d_request.id[12:15]
		d_request.status = '1'
		# d_request.o_URL = 'NULL'
		d_request.requestunit = '江苏省人民政府办公厅'
		if d_request.pk is not None:
			d_request.delete()
		self.assertIsNone(d_request.pk)
		d_request.save()
		self.assertIsNotNone(d_request.pk)
		if d_request.pk is not None:
			d_request.delete()
		return





