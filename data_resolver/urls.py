from django.urls import path
from . import views

urlpatterns = [
    # 最简单的html界面示例(20200502)
    path('index_20200504',views.index_20200504,name='index_20200504'),
    path('index_20200514',views.index_20200514,name='index_20200514'),
    path('index_20200519',views.index_20200519,name='index_20200519'),
    path('details_xmxx',views.details_xmxx,name='details_xmxx'),
    path('index',views.index,name='index'),

    path('register',views.register,name='register'),
    path('registerResponse',views.registerResponse,name='registerResponse'),

    path('login',views.login,name='login'),
    path('loginResponse',views.loginResponse,name='loginResponse'),

	path('deleteuser', views.deleteuser, name='deleteuser'),
	path('deleteuserResponse', views.deleteuserResponse, name='deleteuserResponse'),

	path('uploadfile', views.uploadfile, name='uploadfile'),

    # 人员伤亡
    path('details_DeathStatics',views.details_DeathStatics,name='details_DeathStatics'),
    path('del_DeathStatics',views.del_DeathStatics,name="del_DeathStatics"),
    path('insert_DeathStatics',views.insert_DeathStatics,name="insert_DeathStatics"),
    path('del_DeathStatics',views.insert_DeathStatics,name="insert_DeathStatics"),
    
    # 人员受伤
    path('details_InjuredStatics',views.details_InjuredStatics,name="details_InjuredStatics"),
	path('del_InjuredStatics',views.del_InjuredStatics,name="del_InjuredStatics"),
	path('insert_InjuredStatics',views.insert_InjuredStatics,name="insert_InjuredStatics"),
    
    # 人员失踪
    path('details_MissingStatics',views.details_MissingStatics,name="details_MissingStatics"),
	path('del_MissingStatics',views.del_MissingStatics,name="del_MissingStatics"),
	path('insert_MissingStatics',views.insert_MissingStatics,name="insert_MissingStatics"),

    #土木结构房屋破坏统计表
    path('details_CivilStructure',views.details_CivilStructure,name="details_CivilStructure"),
	path('del_CivilStructure',views.del_CivilStructure,name="del_CivilStructure"),
	path('insert_CivilStructure',views.insert_CivilStructure,name="insert_CivilStructure"),
    #砖木结构房屋破坏统计表
    path('details_BrickwoodStructure',views.details_BrickwoodStructure,name="details_BrickwoodStructure"),
	path('del_BrickwoodStructure',views.del_BrickwoodStructure,name="del_BrickwoodStructure"),
	path('insert_BrickwoodStructure',views.insert_BrickwoodStructure,name="insert_BrickwoodStructure"),
    #砖混结构房屋破坏统计表s
    path('details_MasonryStructure',views.details_MasonryStructure,name="details_MasonryStructure"),
	path('del_MasonryStructure',views.del_MasonryStructure,name="del_MasonryStructure"),
	path('insert_MasonryStructure',views.insert_MasonryStructure,name="insert_MasonryStructure"),
    #框架结构房屋破坏统计表
    path('details_FrameworkStructure',views.details_FrameworkStructure,name="details_FrameworkStructure"),
	path('del_FrameworkStructure',views.del_FrameworkStructure,name="del_FrameworkStructure"),
	path('insert_FrameworkStructure',views.insert_FrameworkStructure,name="insert_FrameworkStructure"),
    #其他结构房屋破坏统计表
    path('details_OtherStructure',views.details_OtherStructure,name="details_OtherStructure"),
	path('del_OtherStructure',views.del_OtherStructure,name="del_OtherStructure"),
	path('insert_OtherStructure',views.insert_OtherStructure,name="insert_OtherStructure"),

    # 通信系统灾情统计表
    path('details_CommDisaster',views.details_CommDisaster,name="details_CommDisaster"),
	path('del_CommDisaster',views.del_CommDisaster,name="del_CommDisaster"),
	path('insert_CommDisaster',views.insert_CommDisaster,name="insert_CommDisaster"),
    # 交通系统灾情统计表
    path('details_TrafficDisaster',views.details_TrafficDisaster,name="details_TrafficDisaster"),
	path('del_TrafficDisaster',views.del_TrafficDisaster,name="del_TrafficDisaster"),
	path('insert_TrafficDisaster',views.insert_TrafficDisaster,name="insert_TrafficDisaster"),
    # 供水系统灾情统计表
    path('details_WaterDisaster',views.details_WaterDisaster,name="details_WaterDisaster"),
	path('del_WaterDisaster',views.del_WaterDisaster,name="del_WaterDisaster"),
	path('insert_WaterDisaster',views.insert_WaterDisaster,name="insert_WaterDisaster"),
    # 输油系统灾情统计表
    path('details_OilDisaster',views.details_OilDisaster,name="details_OilDisaster"),
	path('del_OilDisaster',views.del_OilDisaster,name="del_OilDisaster"),
	path('insert_OilDisaster',views.insert_OilDisaster,name="insert_OilDisaster"),
    # 燃气系统灾情统计表
    path('details_GasDisaster',views.details_GasDisaster,name="details_GasDisaster"),
	path('del_GasDisaster',views.del_GasDisaster,name="del_GasDisaster"),
	path('insert_GasDisaster',views.insert_GasDisaster,name="insert_GasDisaster"),
    # 电力系统灾情统计表    
    path('details_PowerDisaster',views.details_PowerDisaster,name="details_PowerDisaster"),
	path('del_PowerDisaster',views.del_PowerDisaster,name="del_PowerDisaster"),
	path('insert_PowerDisaster',views.insert_PowerDisaster,name="insert_PowerDisaster"),
    # 水利系统灾情统计表
    path('details_IrrigationDisaster',views.details_IrrigationDisaster,name="details_IrrigationDisaster"),
	path('del_IrrigationDisaster',views.del_IrrigationDisaster,name="del_IrrigationDisaster"),
	path('insert_IrrigationDisaster',views.insert_IrrigationDisaster,name="insert_IrrigationDisaster"),

    #崩塌记录表
    path('details_CollapseRecord',views.details_CollapseRecord,name="details_CollapseRecord"),
	path('del_CollapseRecord',views.del_CollapseRecord,name="del_CollapseRecord"),
	path('insert_CollapseRecord',views.insert_CollapseRecord,name="insert_CollapseRecord"),
    #滑坡记录表
    path('details_LandslideRecord',views.details_LandslideRecord,name="details_LandslideRecord"),
	path('del_LandslideRecord',views.del_LandslideRecord,name="del_LandslideRecord"),
	path('insert_LandslideRecord',views.insert_LandslideRecord,name="insert_LandslideRecord"),
    #泥石流记录表
    path('details_DebrisRecord',views.details_DebrisRecord,name="details_DebrisRecord"),
	path('del_DebrisRecord',views.del_DebrisRecord,name="del_DebrisRecord"),
	path('insert_DebrisRecord',views.insert_DebrisRecord,name="insert_DebrisRecord"),
    #岩溶塌陷记录表
    path('details_KarstRecord',views.details_KarstRecord,name="details_KarstRecord"),
	path('del_KarstRecord',views.del_KarstRecord,name="del_KarstRecord"),
	path('insert_KarstRecord',views.insert_KarstRecord,name="insert_KarstRecord"),
    #地裂缝记录表
    path('details_CrackRecord',views.details_CrackRecord,name="details_CrackRecord"),
	path('del_CrackRecord',views.del_CrackRecord,name="del_CrackRecord"),
	path('insert_CrackRecord',views.insert_CrackRecord,name="insert_CrackRecord"),
    #地面沉降记录表
    path('details_SettlementRecord',views.details_SettlementRecord,name="details_SettlementRecord"),
	path('del_SettlementRecord',views.del_SettlementRecord,name="del_SettlementRecord"),
	path('insert_SettlementRecord',views.insert_SettlementRecord,name="insert_SettlementRecord"),
    #其他次生灾害记录表
    path('details_OtherRecord',views.details_OtherRecord,name="details_OtherRecord"),
	path('del_OtherRecord',views.del_OtherRecord,name="del_OtherRecord"),
	path('insert_OtherRecord',views.insert_OtherRecord,name="insert_OtherRecord"),

    #基本震情
    path('details_DisasterInfo',views.details_DisasterInfo,name="details_DisasterInfo"),
	path('del_DisasterInfo',views.del_DisasterInfo,name="del_DisasterInfo"),
	path('insert_DisasterInfo',views.insert_DisasterInfo,name="insert_DisasterInfo"),
    #灾情预测
    path('details_DisatserPrediction',views.details_DisatserPrediction,name="details_DisatserPrediction"),
	path('del_DisatserPrediction',views.del_DisatserPrediction,name="del_DisatserPrediction"),
	path('insert_DisatserPrediction',views.insert_DisatserPrediction,name="insert_DisatserPrediction"),

    #向请求方输出地灾情数据信息表
    path('details_DisasterRequest',views.details_DisasterRequest,name="details_DisasterRequest"),
	path('del_DisasterRequest',views.del_DisasterRequest,name="del_DisasterRequest"),
	path('insert_DisasterRequest',views.insert_DisasterRequest,name="insert_DisasterRequest"),
]