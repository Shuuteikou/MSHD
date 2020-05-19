from django.db import models

#####人员伤亡及失踪数据库设计表#####
#人员伤亡
class DeathStatics(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #死亡人数 最大长度=5（似乎无用）
    number = models.IntegerField()
    #上报单位
    reporting_unit=models.CharField(max_length=50)

#人员失踪
class MissingStatics(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #死亡人数 最大长度=5（似乎无用）
    number = models.IntegerField()
    #上报单位
    reporting_unit=models.CharField(max_length=50)

#####房屋破坏数据库设计表#####
#土木结构房屋破坏统计表
class CivilStructure(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #基本完好面积 单位平方米
    basically_intact_square = models.CharField(max_length=6)
    #破坏面积 单位平方米
    damaged_square = models.CharField(max_length=6)
    #毁坏面积 单位平方米
    destroyed_square = models.CharField(max_length=6)
    #破坏情况描述
    note = models.CharField(max_length=200)
    #上报单位
    reporting_unit=models.CharField(max_length=50)

#砖混结构房屋破坏统计表
class MasonryStructure(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #基本完好面积 单位平方米
    basically_intact_square = models.CharField(max_length=6)
    #轻微破坏面积 单位平方米
    slight_damaged_square = models.CharField(max_length=6)
    #中等破坏面积 单位平方米
    moderate_damaged_square = models.CharField(max_length=6)
    #严重破坏面积 单位平方米
    serious_damaged_square = models.CharField(max_length=6)
    #毁坏面积 单位平方米
    destroyed_square = models.CharField(max_length=6)
    #破坏情况描述
    note = models.CharField(max_length=200)
    #上报单位
    reporting_unit=models.CharField(max_length=50)

#####生命线灾情数据库设计表#####
#通信系统灾情统计表
class CommDisaster(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #属性代码规定： I.中心控制室 II.通信线路
    type = models.CharField(max_length=4)
    #代码规定：I：基本完好 II：轻微破坏 III：中等破坏 IV：严重破坏 V：毁坏
    grade = models.CharField(max_length=4)
    #单张照片≤1mb 格式：jpg
    picture = models.BinaryField(max_length=1024 * 1024 * 8)
    #灾情描述
    note = models.CharField(max_length=200)
    #上报单位
    reporting_unit=models.CharField(max_length=50)

#交通系统灾情统计表
class TrafficDisaster(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #属性代码规定： I.中心控制室 II.通信线路
    type = models.CharField(max_length=4)
    #代码规定：I：基本完好 II：轻微破坏 III：中等破坏 IV：严重破坏 V：毁坏
    grade = models.CharField(max_length=4)
    #单张照片≤1mb 格式：jpg
    picture = models.BinaryField(max_length=1024 * 1024 * 8)
    #灾情描述
    note = models.CharField(max_length=200)
    #上报单位
    reporting_unit=models.CharField(max_length=50)

#####次生灾害数据库设计表#####
#崩塌记录表
class CollapseRecord(models.Model):
    # 编码
    id = models.CharField(max_length=19,primary_key=True)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #类型 属性代码规定： Ⅰ.特大型 Ⅱ.大型 Ⅲ.中型 Ⅳ.小型
    type = models.CharField(max_length=10)
    #灾害程度 属性代码规定： Ⅰ.特大型 Ⅱ.大型 Ⅲ.中型 Ⅳ.小型
    status = models.CharField(max_length=10)
    #灾情描述
    note = models.CharField(max_length=200)
    #单张照片≤1mb 格式：jpg
    picture = models.BinaryField(max_length=1024 * 1024 * 8)
    # 上报单位
    reporting_unit = models.CharField(max_length=50)

#滑坡记录表
class LandslideRecord(models.Model):
    # 编码
    id = models.CharField(max_length=19,primary_key=True)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #类型 属性代码规定： Ⅰ.特大型 Ⅱ.大型 Ⅲ.中型 Ⅳ.小型
    type = models.CharField(max_length=10)
    #灾害程度 属性代码规定： Ⅰ.特大型 Ⅱ.大型 Ⅲ.中型 Ⅳ.小型
    status = models.CharField(max_length=10)
    #灾情描述
    note = models.CharField(max_length=200)
    #单张照片≤1mb 格式：jpg
    picture = models.BinaryField(max_length=1024 * 1024 * 8)
    # 上报单位
    reporting_unit = models.CharField(max_length=50)

#####震情数据库设计表#####
#基本震情
class DisasterInfo(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #经度 float
    longtitude = models.FloatField(max_length=100)
    #纬度
    latitude = models.FloatField(max_length=100)
    #深度
    depth = models.FloatField(max_length=100)
    #震级
    magnitude = models.FloatField(max_length=100)
    #单张照片≤1mb 格式：jpg
    picture = models.BinaryField(max_length=1024 * 1024 * 8)
    #上报单位
    reporting_unit = models.CharField(max_length=50)


#灾情预测
class DisatserPrediction(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #地点:州市+县区+（乡镇+行政村）+具体地点描述
    location = models.CharField(max_length=100)
    #经度 float
    longtitude = models.FloatField(max_length=100)
    #纬度
    latitude = models.FloatField(max_length=100)
    #深度
    depth = models.FloatField(max_length=100)
    #震级
    magnitude = models.FloatField(max_length=100)
    #烈度（地震对地表及工程建筑物影响的强弱程度） ->中国的12度表制
    Intensity = models.CharField(max_length=6)
    #类型 代码规定：1：天然地震 2：人为破坏引发 3： 海啸引发 4：火山引发 5：其他
    type = models.CharField(max_length=2)
    # 灾情描述（破坏情况描述）
    note = models.CharField(max_length=200)
    #单张照片≤1mb 格式：jpg
    picture = models.BinaryField(max_length=1024 * 1024 * 8)
    # 上报单位
    reporting_unit = models.CharField(max_length=50)


#向请求方输出地灾情数据信息表
class DisasterRequest(models.Model):
    #编码
    id = models.CharField(max_length=19,primary_key=True)
    #上报时间:日期(日-月-年) DD-MM-YY(HH-MISS) - 24小时制
    date = models.CharField(max_length=12)
    #请求灾情类型(详见表1 - 灾情信息分类表)
    disasterType = models.CharField(max_length=3)
    #状态 取值规范： 0：未发送 1：已发送
    status = models.CharField(max_length=1)
    #发送地址
    o_URL = models.CharField(max_length=200)
    #请求单位
    requestunit = models.CharField(max_length=50)