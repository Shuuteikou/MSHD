from django.test import TestCase
"""
from data_resolver.models import DeathStatics, InjuredStatics, MissingStatics
from data_resolver.models import CivilStructure, BrickwoodStructure, MasonryStructure, FrameworkStructure, OtherStructure
from data_resolver.models import CommDisaster, TrafficDisaster, WaterDisaster, OilDisaster, GasDisaster, PowerDisaster, IrrigationDisaster
from data_resolver.models import CollapseRecord, LandslideRecord, DebrisRecord, KarstRecord, CrackRecord, SettlementRecord, OtherRecord
from data_resolver.models import DisasterInfo, DisatserPrediction,  DisasterRequest

class ModelTest(TestCase):

	#根据灾情信息的大类和子类编码，确定数据存入的数据表
	def test_disaster_type_choose (self):
		fake_id = '0101010020041111101' #此处应当从前端传来的json文件中获取真实的id
		disastertype_num = fake_id[12:15]
		if disastertype_num == '111':
			test_can_insert_in_DeathStatics(self)
		elif disastertype_num == '112':
			test_can_insert_in_InjuredStatics(self)
		elif disastertype_num == '113':
			test_can_insert_in_MissingStatics(self)
		elif disastertype_num == '221':
			test_can_insert_in_CivilStructure(self)
		elif disastertype_num == '222':
			test_can_insert_in_BrickwoodStructure(self)
		elif disastertype_num == '223':
			test_can_insert_in_MasonryStructure(self)
		elif disastertype_num == '224':
			test_can_insert_in_FrameworkStructure(self)
		elif disastertype_num == '225':
			test_can_insert_in_OtherStructure(self)
		elif disastertype_num == '331':
			test_can_insert_in_TrafficDisaster(self)
		elif disastertype_num == '332':
			test_can_insert_in_WaterDisaster(self)
		elif disastertype_num == '333':
			test_can_insert_in_OilDisaster(self)
		elif disastertype_num == '334':
			test_can_insert_in_GasDisaster(self)
		elif disastertype_num == '335':
			test_can_insert_in_PowerDisaster(self)
		elif disastertype_num == '336':
			test_can_insert_in_CommDisaster(self)
		elif disastertype_num == '337':
			test_can_insert_in_IrrigationDisaster(self)
		elif disastertype_num == '441':
			test_can_insert_in_CollapseRecord(self)
		elif disastertype_num == '442':
			test_can_insert_in_LandslideRecord(self)
		elif disastertype_num == '443':
			test_can_insert_in_DebrisRecord(self)
		elif disastertype_num == '444':
			test_can_insert_in_KarstRecord(self)
		elif disastertype_num == '445':
			test_can_insert_in_CrackRecord(self)
		elif disastertype_num == '446':
			test_can_insert_in_SettlementRecord(self)
		elif disastertype_num == '447':
			test_can_insert_in_OtherRecord(self)
		elif disastertype_num == '551':
			test_can_insert_in_DisasterInfo(self)
		elif disastertype_num == '552':
			test_can_insert_in_DisasterPrediction(self)

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
        
    def test_can_insert_in_DeathStatics_2(self):
		d_statics = DeathStatics()
		d_statics.id = '5118242010001111111'
		d_statics.location = '四川省雅安市石棉县先锋藏族乡'
		d_statics.date = '2020-05-03 18:06:12'
		d_statics.number = '173'
		d_statics.reporting_unit = '2201' + '四川省人民政府办公厅'
		if d_statics.pk is not None:
			d_statics.delete()
		self.assertIsNone(d_statics.pk)
		d_statics.save()
		self.assertIsNotNone(d_statics.pk)
		if d_statics.pk is not None:
			d_statics.delete()
		return
        
    def test_can_insert_in_DeathStatics_3(self):
		d_statics = DeathStatics()
		d_statics.id = '1403111010001111111'
		d_statics.location = '山西省阳泉市郊区河底镇 '
		d_statics.date = '2020-05-13 08:06:12'
		d_statics.number = '103'
		d_statics.reporting_unit = '1103' + '山西省人民政府办公厅'
		if d_statics.pk is not None:
			d_statics.delete()
		self.assertIsNone(d_statics.pk)
		d_statics.save()
		self.assertIsNotNone(d_statics.pk)
		if d_statics.pk is not None:
			d_statics.delete()
		return


	#InjuredStatics
	def test_can_insert_in_InjuredStatics(self):
		i_statics = InjuredStatics()
		i_statics.id = '0101010020041121101'
		i_statics.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		i_statics.date = '2020-05-20 12:12:12'
		i_statics.number = '200'
		i_statics.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if i_statics.pk is not None:
			i_statics.delete()
		self.assertIsNone(i_statics.pk)
		i_statics.save()
		self.assertIsNotNone(i_statics.pk)
		if i_statics.pk is not None:
			i_statics.delete()
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
    
        
    def test_can_insert_in_MissingStatics_2(self):
		m_statics = MissingStatics()
		m_statics.id = '5118242010001131101'
		m_statics.location = '四川省雅安市石棉县先锋藏族乡'
		m_statics.date = '2020-05-03 18:06:12'
		m_statics.number = '17'
		m_statics.reporting_unit = '2201' + '四川省人民政府办公厅'
		if m_statics.pk is not None:
			m_statics.delete()
		self.assertIsNone(m_statics.pk)
		m_statics.save()
		self.assertIsNotNone(m_statics.pk)
		if m_statics.pk is not None:
			m_statics.delete()
		return    

    def test_can_insert_in_MissingStatics_3(self):
		m_statics = MissingStatics()
		m_statics.id = '1403111010001131101'
		m_statics.location = '山西省阳泉市郊区河底镇 '
		m_statics.date = '2020-05-03 18:06:12'
		m_statics.number = '17'
		m_statics.reporting_unit = '1103' + '山西省人民政府办公厅'
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
        
    def test_can_insert_in_CivilStructure_2(self):
		c_structure = CivilStructure()
		c_structure.id = '5118242010002210011'
		c_structure.date = '2020-05-20 12:12:12'
		c_structure.location = '四川省雅安市石棉县先锋藏族乡'
		c_structure.basically_intact_square = '2500'
		c_structure.damaged_square = '2000'
		c_structure.destroyed_square = '1000'
		c_structure.note = '破坏情况严重'
		c_structure.reporting_unit = '2201' + '四川省人民政府办公厅'
		if c_structure.pk is not None:
			c_structure.delete()
		self.assertIsNone(c_structure.pk)
		c_structure.save()
		self.assertIsNotNone(c_structure.pk)
		if c_structure.pk is not None:
			c_structure.delete()
		return
        
    def test_can_insert_in_CivilStructure_3(self):
		c_structure = CivilStructure()
		c_structure.id = '1403111010002210011'
		c_structure.date = '2020-05-03 18:06:12'
		c_structure.location = '山西省阳泉市郊区河底镇'
		c_structure.basically_intact_square = '5000'
		c_structure.damaged_square = '2500'
		c_structure.destroyed_square = '1500'
		c_structure.note = '破坏情况严重'
		c_structure.reporting_unit = '1103' + '山西省人民政府办公厅'
		if c_structure.pk is not None:
			c_structure.delete()
		self.assertIsNone(c_structure.pk)
		c_structure.save()
		self.assertIsNotNone(c_structure.pk)
		if c_structure.pk is not None:
			c_structure.delete()
		return


	#BrickwoodStructure
	def test_can_insert_in_BrickwoodStructure(self):
		b_structure = BrickwoodStructure()
		b_structure.id = '0101010020042221101'
		b_structure.date = '2020-05-20 12:12:12'
		b_structure.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		b_structure.basically_intact_square = '3000'
		b_structure.damaged_square = '1250'
		b_structure.destroyed_square = '1200'
		b_structure.note = '破坏情况比较严重'
		b_structure.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if b_structure.pk is not None:
			b_structure.delete()
		self.assertIsNone(b_structure.pk)
		b_structure.save()
		self.assertIsNotNone(b_structure.pk)
		if b_structure.pk is not None:
			b_structure.delete()
		return

	#MasonryStructure
	def test_can_insert_in_MasonryStructure(self):
		m_structure = MasonryStructure()
		m_structure.id = '0101010020042231101'
		m_structure.date = '2020-05-03 18:06:12'
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
        
    def test_can_insert_in_MasonryStructure_2(self):
		m_structure = MasonryStructure()
		m_structure.id = '511824201002231100'
		m_structure.date = '2020-05-20 12:12:12'
		m_structure.location = '四川省雅安市石棉县先锋藏族乡'
		m_structure.basically_intact_square = '3000',
		m_structure.slight_damaged_square = '1000'
		m_structure.moderate_damaged_square = '500'
		m_structure.serious_damaged_square = '300'
		m_structure.destroyed_square = '400'
		m_structure.note = '破坏情况严重'
		m_structure.reporting_unit = '2201' + '四川省人民政府办公厅'
		if m_structure.pk is not None:
			m_structure.delete()
		self.assertIsNone(m_structure.pk)
		m_structure.save()
		self.assertIsNotNone(m_structure.pk)
		if m_structure.pk is not None:
			m_structure.delete()
		return


     def test_can_insert_in_MasonryStructure_3(self):
		m_structure = MasonryStructure()
		m_structure.id = '140311101002231100'
		m_structure.date = '2020-05-13 08:06:12'
		m_structure.location = '山西省阳泉市郊区河底镇'
		m_structure.basically_intact_square = '2000',
		m_structure.slight_damaged_square = '500'
		m_structure.moderate_damaged_square = '300'
		m_structure.serious_damaged_square = '200'
		m_structure.destroyed_square = '500'
		m_structure.note = '情况比较严重'
		m_structure.reporting_unit = '1103' + '山西省人民政府办公厅'
		if m_structure.pk is not None:
			m_structure.delete()
		self.assertIsNone(m_structure.pk)
		m_structure.save()
		self.assertIsNotNone(m_structure.pk)
		if m_structure.pk is not None:
			m_structure.delete()
		return


	#FrameworkStructure
	def test_can_insert_in_FrameworkStructure(self):
		f_structure = FrameworkStructure()
		f_structure.id = '0101010020042241101'
		f_structure.date = '2020-05-03 18:06:12'
		f_structure.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		f_structure.basically_intact_square = '3000'
		f_structure.slight_damaged_square = '300'
		f_structure.moderate_damaged_square = '300'
		f_structure.serious_damaged_square = '300'
		f_structure.destroyed_square = '400'
		f_structure.note = '破坏情况比较严重'
		f_structure.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if f_structure.pk is not None:
			f_structure.delete()
		self.assertIsNone(f_structure.pk)
		f_structure.save()
		self.assertIsNotNone(f_structure.pk)
		if f_structure.pk is not None:
			f_structure.delete()
		return 

	#OtherStructure
	def test_can_insert_in_OtherStructure(self):
		o_structure = OtherStructure()
		o_structure.id = '0101010020042251101'
		o_structure.date = '2020-05-03 18:06:12'
		o_structure.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		o_structure.basically_intact_square = '3000'
		o_structure.slight_damaged_square = '300'
		o_structure.moderate_damaged_square = '300'
		o_structure.serious_damaged_square = '300'
		o_structure.destroyed_square = '400'
		o_structure.note = '破坏情况比较严重'
		o_structure.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if o_structure.pk is not None:
			o_structure.delete()
		self.assertIsNone(o_structure.pk)
		o_structure.save()
		self.assertIsNotNone(o_structure.pk)
		if o_structure.pk is not None:
			o_structure.delete()
		return 

	#CommDisaster
	def test_can_insert_in_CommDisaster(self):
		c_disaster = CommDisaster()
		c_disaster.id = '0101010020043362202'
		c_disaster.date = '2007-06-05 12:12:12'
		c_disaster.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		c_disaster.type = '1'
		c_disaster.grade = '2'
		# fp = open("data_resolver/pic/pic_example.jpg", 'rb')
		# c_disaster.picture = fp.read()
		# fp.close()
		# c_disaster.picture = NULL
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
    
    def test_can_insert_in_CommDisaster_2(self):
		c_disaster = CommDisaster()
		c_disaster.id = '5118242010003361110'
		c_disaster.date = '2020-05-20 12:12:12'
		c_disaster.location = '四川省雅安市石棉县先锋藏族乡'
		c_disaster.type = '2'
		c_disaster.grade = '2'
		c_disaster.note = '严重'
		c_disaster.reporting_unit = '2201' + '四川省人民政府办公厅'
		if c_disaster.pk is not None:
			c_disaster.delete()
		self.assertIsNone(c_disaster.pk)
		c_disaster.save()
		self.assertIsNotNone(c_disaster.pk)
		if c_disaster.pk is not None:
			c_disaster.delete()
		return
        
    def test_can_insert_in_CommDisaster_3(self):
		c_disaster = CommDisaster()
		c_disaster.id = '1403111010003361110'
		c_disaster.date = '2020-05-03 18:06:12'
		c_disaster.location = '山西省阳泉市郊区河底镇'
		c_disaster.type = '1'
		c_disaster.grade = '2'
		c_disaster.note = '严重'
		c_disaster.reporting_unit = '1103' + '山西省人民政府办公厅'
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
		if t_disaster.pk is not None:
			t_disaster.delete()
		self.assertIsNone(t_disaster.pk)
		t_disaster.save()
		self.assertIsNotNone(t_disaster.pk)
		if t_disaster.pk is not None:
			t_disaster.delete()
		return
        
    def test_can_insert_in_TrafficDisaster_2(self):
		t_disaster = TrafficDisaster()
		t_disaster.id = '5118242010003312022'
		t_disaster.date = '2020-05-20 12:12:12'
		t_disaster.location = '四川省雅安市石棉县先锋藏族乡'
		t_disaster.type = '2'
		t_disaster.grade = '1'
		# t_disaster.picture = NULL 
		t_disaster.note = '严重'
		t_disaster.reporting_unit = '2201' + '四川省人民政府办公厅'
		if t_disaster.pk is not None:
			t_disaster.delete()
		self.assertIsNone(t_disaster.pk)
		t_disaster.save()
		self.assertIsNotNone(t_disaster.pk)
		if t_disaster.pk is not None:
			t_disaster.delete()
		return
        
    def test_can_insert_in_TrafficDisaster_3(self):
		t_disaster = TrafficDisaster()
		t_disaster.id = '1403111010003312022'
		t_disaster.date = '2020-05-03 18:06:12'
		t_disaster.location = '山西省阳泉市郊区河底镇'
		t_disaster.type = '1'
		t_disaster.grade = '1'
		# t_disaster.picture = NULL 
		t_disaster.note = '严重'
		t_disaster.reporting_unit = '1103' + '山西省人民政府办公厅'
		if t_disaster.pk is not None:
			t_disaster.delete()
		self.assertIsNone(t_disaster.pk)
		t_disaster.save()
		self.assertIsNotNone(t_disaster.pk)
		if t_disaster.pk is not None:
			t_disaster.delete()
		return

	#WaterDisaster
	def test_can_insert_in_WaterDisaster(self):
	    w_disaster = WaterDisaster()
	    w_disaster.id = '0101010020043322202'
		w_disaster.date = '2007-06-05 12:12:12'
		w_disaster.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		w_disaster.type = '1'
		w_disaster.grade = '2'
		# w_disaster.picture = NULL 
		w_disaster.note = '严重'
		w_disaster.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if w_disaster.pk is not None:
			w_disaster.delete()
		self.assertIsNone(w_disaster.pk)
		w_disaster.save()
		self.assertIsNotNone(w_disaster.pk)
		if w_disaster.pk is not None:
			w_disaster.delete()
		return

	#Oildisaster
	def test_can_insert_in_OilDisaster(self):
		o_disaster = Oildisaster()
		o_disaster.id = '0101010020043332202'
		o_disaster.date = '2007-06-05 12:12:12'
		o_disaster.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		o_disaster.type = '1'
		o_disaster.grade = '2'
		# o_disaster.picture = NULL 
		o_disaster.note = '严重'
		o_disaster.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if o_disaster.pk is not None:
			o_disaster.delete()
		self.assertIsNone(o_disaster.pk)
		o_disaster.save()
		self.assertIsNotNone(o_disaster.pk)
		if o_disaster.pk is not None:
			o_disaster.delete()
		return

	#GasDisaster
	def test_can_insert_in_GasDisaster(self):
		g_disaster = GasDisaster()
		g_disaster.id = '0101010020043342202'
		g_disaster.date = '2007-06-05 12:12:12'
		g_disaster.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		g_disaster.type = '1'
		g_disaster.grade = '2'
		# g_disaster.picture = NULL 
		g_disaster.note = '严重'
		g_disaster.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if g_disaster.pk is not None:
			g_disaster.delete()
		self.assertIsNone(g_disaster.pk)
		g_disaster.save()
		self.assertIsNotNone(g_disaster.pk)
		if g_disaster.pk is not None:
			g_disaster.delete()
		return

	#PowerDisaster
	def test_can_insert_in_PowerDisaster(self):
		p_disaster = PowerDisaster()
		p_disaster.id = '0101010020043352202'
		p_disaster.date = '2007-06-05 12:12:12'
		p_disaster.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		p_disaster.type = '1'
		p_disaster.grade = '2'
		# p_disaster.picture = NULL 
		p_disaster.note = '严重'
		p_disaster.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if p_disaster.pk is not None:
			p_disaster.delete()
		self.assertIsNone(p_disaster.pk)
		p_disaster.save()
		self.assertIsNotNone(p_disaster.pk)
		if p_disaster.pk is not None:
			p_disaster.delete()
		return

	#IrrigationDisaster
	def test_can_insert_in_IrrigationDisaster(self):
		i_disaster = IrrigationDisaster()
		i_disaster.id = '0101010020043372202'
		i_disaster.date = '2007-06-05 12:12:12'
		i_disaster.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		i_disaster.type = '1'
		i_disaster.grade = '2'
		# i_disaster.picture = NULL 
		i_disaster.note = '严重'
		i_disaster.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if i_disaster.pk is not None:
			i_disaster.delete()
		self.assertIsNone(i_disaster.pk)
		i_disaster.save()
		self.assertIsNotNone(i_disaster.pk)
		if i_disaster.pk is not None:
			i_disaster.delete()
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
        
    def test_can_insert_in_CollapseRecord_2(self):
		c_record = CollapseRecord()
		c_record.id = '5118242010004412021'
		c_record.location = '四川省雅安市石棉县先锋藏族乡'
		c_record.date = '2020-05-20 12:12:12'
		c_record.type = '1'
		c_record.status = '1'
		c_record.note = '严重'
		# c_record.picture = NULL
		c_record.reporting_unit = '2201' + '四川省人民政府办公厅'
		if c_record.pk is not None:
			c_record.delete()
		self.assertIsNone(c_record.pk)
		c_record.save()
		self.assertIsNotNone(c_record.pk)
		if c_record.pk is not None:
			c_record.delete()
		return

    def test_can_insert_in_CollapseRecord_3(self):
		c_record = CollapseRecord()
		c_record.id = '5118242010004412021'
		c_record.location = '山西省阳泉市郊区河底镇'
		c_record.date = '2020-05-03 18:06:12'
		c_record.type = '1'
		c_record.status = '2'
		c_record.note = '严重'
		# c_record.picture = NULL
		c_record.reporting_unit = '1103' + '山西省人民政府办公厅'
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
		l_record.id = '0101010020044422202'
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
        
    def test_can_insert_in_LandslideRecord_2(self):
		l_record = LandslideRecord()
		l_record.id = '5118242010004422020'
		l_record.location = '四川省雅安市石棉县先锋藏族乡'
		l_record.date = '2020-05-20 12:12:12'
		l_record.type = '2'
		l_record.status = '2'
		l_record.note = '较为严重'
		# l_record.picture = NULL
		l_record.reporting_unit = '2201' + '四川省人民政府办公厅'
		if l_record.pk is not None:
			l_record.delete()
		self.assertIsNone(l_record.pk)
		l_record.save()
		self.assertIsNotNone(l_record.pk)
		if l_record.pk is not None:
			l_record.delete()
		return
        
    def test_can_insert_in_LandslideRecord_3(self):
		l_record = LandslideRecord()
		l_record.id = '1403111010004422020'
		l_record.location = '山西省阳泉市郊区河底镇'
		l_record.date = '2020-05-03 18:06:12'
		l_record.type = '1'
		l_record.status = '2'
		l_record.note = '较为严重'
		# l_record.picture = NULL
		l_record.reporting_unit = '1103' + '山西省人民政府办公厅'
		if l_record.pk is not None:
			l_record.delete()
		self.assertIsNone(l_record.pk)
		l_record.save()
		self.assertIsNotNone(l_record.pk)
		if l_record.pk is not None:
			l_record.delete()
		return
    
    #DebrisRecord
    def test_can_insert_in_DebrisRecord(self):
    	d_record = DebrisRecord()
    	d_record.id = '0101010020044432202'
		d_record.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		d_record.date = '2020-05-20 12:12:12'
		d_record.type = '2'
		d_record.status = '2'
		d_record.note = '较为严重'
		# d_record.picture = NULL
		d_record.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if d_record.pk is not None:
			d_record.delete()
		self.assertIsNone(d_record.pk)
		d_record.save()
		self.assertIsNotNone(d_record.pk)
		if d_record.pk is not None:
			d_record.delete()
		return


	#KarstRecord
	def test_can_insert_in_KarstRecord(self):
		k_record = KarstRecord()
		k_record.id = '0101010020044442202'
		k_record.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		k_record.date = '2020-05-20 12:12:12'
		k_record.type = '2'
		k_record.status = '2'
		k_record.note = '较为严重'
		# k_record.picture = NULL
		k_record.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if k_record.pk is not None:
			k_record.delete()
		self.assertIsNone(k_record.pk)
		k_record.save()
		self.assertIsNotNone(k_record.pk)
		if k_record.pk is not None:
			k_record.delete()
		return

	#CrackRecord
	def test_can_insert_in_CrackRecord(self):
		c_record = CrackRecord()
		c_record.id = '0101010020044452202'
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

	#SettlementRecord
	def test_can_insert_in_SettlementRecord(self):
		s_record = SettlementRecord()
		s_record.id = '0101010020044462202'
		s_record.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		s_record.date = '2020-05-20 12:12:12'
		s_record.type = '2'
		s_record.status = '2'
		s_record.note = '较为严重'
		# s_record.picture = NULL
		s_record.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if s_record.pk is not None:
			s_record.delete()
		self.assertIsNone(s_record.pk)
		s_record.save()
		self.assertIsNotNone(s_record.pk)
		if s_record.pk is not None:
			c_record.delete()
		return


	#OtherRecord
	def test_can_insert_in_OtherRecord(self):
		o_record = OtherRecord()
		o_record.id = '0101010020044472202'
		o_record.location = '江苏省南京市玄武区新街口街道大石桥社区某一区域'
		o_record.date = '2020-05-20 12:12:12'
		o_record.type = '2'
		o_record.status = '2'
		o_record.note = '较为严重'
		# o_record.picture = NULL
		o_record.reporting_unit = '2202' + '江苏省人民政府办公厅'
		if o_record.pk is not None:
			o_record.delete()
		self.assertIsNone(o_record.pk)
		o_record.save()
		self.assertIsNotNone(o_record.pk)
		if s_record.pk is not None:
			c_record.delete()
		return

	#DisasterInfo
	def test_can_insert_in_DisasterInfo(self):
		d_info = DisasterInfo()
		d_info.id = '0101010020045512202'
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
        
    def test_can_insert_in_DisasterInfo_2(self):
		d_info = DisasterInfo()
		d_info.id = '5118242010005511220'
		d_info.date = '2020-05-20 12:12:12'
		d_info.location = '四川省雅安市石棉县先锋藏族乡'
		d_info.longtitude = '102.281929'
		d_info.latitude = '29.280413'
		d_info.depth = '43.45'
		d_info.magnitude = '7'
		# d_info.picture = NULL
		d_info.reporting_unit = '2201' + '四川省人民政府办公厅'
		if d_infp.pk is not None:
			d_info.delete()
		self.assertIsNone(d_info.pk)
		d_info.save()
		self.assertIsNotNone(d_info.pk)
		if d_info.pk is not None:
			d_info.delete()
		return
        
    def test_can_insert_in_DisasterInfo_3(self):
		d_info = DisasterInfo()
		d_info.id = '1403111010005511220'
		d_info.date = '2020-05-13 08:06:12'
		d_info.location = '山西省阳泉市郊区河底镇'
		d_info.longtitude = '113.57'
		d_info.latitude = '38.00'
		d_info.depth = '56.12'
		d_info.magnitude = '7'
		# d_info.picture = NULL
		d_info.reporting_unit = '1103' + '山西省人民政府办公厅'
		if d_infp.pk is not None:
			d_info.delete()
		self.assertIsNone(d_info.pk)
		d_info.save()
		self.assertIsNotNone(d_info.pk)
		if d_info.pk is not None:
			d_info.delete()
		return    


	#DisasterPrediction
	def test_can_insert_in_DisasterPrediction(self):
		d_prediction = DisatserPrediction()
		d_prediction.id = '0101010020045522202'
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
        
    def test_can_insert_in_DisasterPrediction_2(self):
		d_prediction = DisatserPrediction()
		d_prediction.id = '5118242010005521221'
		d_prediction.date = '2020-05-20 12:12:12'
		d_prediction.location = '四川省雅安市石棉县先锋藏族乡'
		d_prediction.longtitude = '102.281929'
		d_prediction.latitude = '29.280413'
		d_prediction.depth = '43.45'
		d_prediction.magnitude = '5.4'
		d_prediction.intensity = '7'
		d_prediction.type = '1'
		d_prediction.note = '受灾严重'
		# d_prediction.picture = '0000'
		d_prediction.reporting_unit = '2201' + '四川省人民政府办公厅'
		if d_prediction.pk is not None:
			d_prediction.delete()
		self.assertIsNone(d_prediction.pk)
		d_prediction.save()
		self.assertIsNotNone(d_prediction.pk)
		if d_prediction.pk is not None:
			d_prediction.delete()
		return
    
    def test_can_insert_in_DisasterPrediction_3(self):
		d_prediction = DisatserPrediction()
		d_prediction.id = '1403111010005521221'
		d_prediction.date = '2020-05-03 18:06:12'
		d_prediction.location = '山西省阳泉市郊区河底镇'
		d_prediction.longtitude = '113.57'
		d_prediction.latitude = '38.00'
		d_prediction.depth = '56.12'
		d_prediction.magnitude = '5.8'
		d_prediction.intensity = '7'
		d_prediction.type = '1'
		d_prediction.note = '受灾严重'
		# d_prediction.picture = '0000'
		d_prediction.reporting_unit = '1103' + '山西省人民政府办公厅'
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
        
    def test_can_insert_in_DisasterRequest_2(self):
		d_request = DisasterRequest()
		d_request.id = '5118242010001131224'
		d_request.date = '2020-05-18 17:36:12'
		d_request.disasterType = d_request.id[12:15]
		d_request.status = '1'
		# d_request.o_URL = 'NULL'
		d_request.requestunit = '四川省人民政府办公厅'
		if d_request.pk is not None:
			d_request.delete()
		self.assertIsNone(d_request.pk)
		d_request.save()
		self.assertIsNotNone(d_request.pk)
		if d_request.pk is not None:
			d_request.delete()
		return


    def test_can_insert_in_DisasterRequest_3(self):
		d_request = DisasterRequest()
		d_request.id = '1403111010001131224'
		d_request.date = '2020-05-03 18:06:12'
		d_request.disasterType = d_request.id[12:15]
		d_request.status = '1'
		# d_request.o_URL = 'NULL'
		d_request.requestunit = '山西省人民政府办公厅'
		if d_request.pk is not None:
			d_request.delete()
		self.assertIsNone(d_request.pk)
		d_request.save()
		self.assertIsNotNone(d_request.pk)
		if d_request.pk is not None:
			d_request.delete()
		return
"""