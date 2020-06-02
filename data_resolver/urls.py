from django.urls import path
from . import views

urlpatterns = [
    # 最简单的html界面示例(20200502)
    path('index_20200504',views.index_20200504,name='index_20200504'),
    path('index_20200514',views.index_20200514,name='index_20200514'),
    path('index_20200519',views.index_20200519,name='index_20200519'),
    path('insert',views.insert_DeathStatics,name="insert_DeathStatics"),
    path('details_xmxx',views.details_xmxx,name='details_xmxx'),
    path('index',views.index,name='index'),
]