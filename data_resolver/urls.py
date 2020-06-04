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

    
]