from django.urls import path
from . import views

urlpatterns = [
    # 最简单的html界面示例(20200502)
    path('index_20200504',views.index_20200504,name='index_20200504'),
    path('index_20200514',views.index_20200514,name='index_20200514'),
    path('index_20200519',views.index_20200519,name='index_20200519'),
    path('insert_DeathStatics',views.insert_DeathStatics,name="insert_DeathStatics"),
    path('insert_InjuredStatics',views.insert_InjuredStatics,name="insert_InjuredStatics"),
    path('details_xmxx',views.details_xmxx,name='details_xmxx'),
    path('index',views.index,name='index'),

    # 人员伤亡
    path('details_DeathStatics',views.details_DeathStatics,name='details_DeathStatics'),
    # 人员受伤
    path('details_InjuredStatics',views.details_InjuredStatics,name="details_InjuredStatics"),
    # 人员失踪
    path('details_MissingStatics',views.details_MissingStatics,name="details_MissingStatics"),

    #土木结构房屋破坏统计表
    path('details_CivilStructure',views.details_CivilStructure,name="details_CivilStructure"),
    #砖木结构房屋破坏统计表
    path('details_BrickwoodStructure',views.details_BrickwoodStructure,name="details_BrickwoodStructure"),
    #砖混结构房屋破坏统计表
    path('details_MasonryStructure',views.details_MasonryStructure,name="details_MasonryStructure"),
    #框架结构房屋破坏统计表
    path('details_FrameworkStructure',views.details_FrameworkStructure,name="details_FrameworkStructure"),
    #其他结构房屋破坏统计表
    path('details_OtherStructure',views.details_OtherStructure,name="details_OtherStructure"),

    # 通信系统灾情统计表
    path('details_CommDisaster',views.details_CommDisaster,name="details_CommDisaster"),
    # 交通系统灾情统计表
    path('details_TrafficDisaster',views.details_TrafficDisaster,name="details_TrafficDisaster"),
    # 供水系统灾情统计表
    path('details_WaterDisaster',views.details_WaterDisaster,name="details_WaterDisaster"),
    # 输油系统灾情统计表
    path('details_OilDisaster',views.details_OilDisaster,name="details_OilDisaster"),
    # 燃气系统灾情统计表
    path('details_GasDisaster',views.details_GasDisaster,name="details_GasDisaster"),
    # 电力系统灾情统计表    
    path('details_PowerDisaster',views.details_PowerDisaster,name="details_PowerDisaster"),
    # 水利系统灾情统计表
    path('details_IrrigationDisaster',views.details_IrrigationDisaster,name="details_IrrigationDisaster"),

    #崩塌记录表
    path('details_CollapseRecord',views.details_CollapseRecord,name="details_CollapseRecord"),
    #滑坡记录表
    path('details_LandslideRecord',views.details_LandslideRecord,name="details_LandslideRecord"),
    #泥石流记录表
    path('details_DebrisRecord',views.details_DebrisRecord,name="details_DebrisRecord"),
    #岩溶塌陷记录表
    path('details_KarstRecord',views.details_KarstRecord,name="details_KarstRecord"),
    #地裂缝记录表
    path('details_CrackRecord',views.details_CrackRecord,name="details_CrackRecord"),
    #地面沉降记录表
    path('details_SettlementRecord',views.details_SettlementRecord,name="details_SettlementRecord"),
    #其他次生灾害记录表
    path('details_OtherRecord',views.details_OtherRecord,name="details_OtherRecord"),

]