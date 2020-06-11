#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.shortcuts import render
from django.core import serializers
#  人员
from .models import DeathStatics, MissingStatics, InjuredStatics
#  房屋
from .models import CivilStructure,  MasonryStructure,  BrickwoodStructure,  FrameworkStructure, OtherStructure
#  生命线
from .models import CommDisaster,  TrafficDisaster, WaterDisaster, OilDisaster, GasDisaster, IrrigationDisaster, PowerDisaster
#  次生灾害
from .models import CollapseRecord, LandslideRecord, DebrisRecord, KarstRecord, CrackRecord, SettlementRecord, OtherRecord
#  震情
from .models import DisasterInfo, DisatserPrediction, DisasterRequest

from django.shortcuts import get_object_or_404,  render, redirect
#  from .models import day, todo

from django.http import JsonResponse
import json

#  Create your views here.
disaster_type_dictionary = {
    '111': DeathStatics, '112':InjuredStatics, '113':MissingStatics,
    '221':CivilStructure,'222':BrickwoodStructure,'223':MasonryStructure,'224':FrameworkStructure,
    '225':OtherStructure,
    '331':TrafficDisaster,'332':WaterDisaster,'333':OilDisaster,'334':GasDisaster,
    '335':PowerDisaster,'336':CommDisaster,'337':IrrigationDisaster,
    '441':CollapseRecord,'442':LandslideRecord,'443':DebrisRecord,
    '444':KarstRecord,'445':CrackRecord,'446':SettlementRecord,'447':OtherStructure,
    '551':DisasterInfo,'552':DisatserPrediction,
}
# 代号和代号类的对应表

# 响应请求信息
def response_disasterType(request):
    #查找所有没有响应的请求
    r = DisasterRequest.objects.filter(status='0')
    data = {}
    if r.exists():
        result = r[0]
        addr = request.o_URL
        if r.DisasterType in disaster_type_dictionary.keys():
            dataType = disaster_type_dictionary[r.DisasterType]
            res = dataType.objects.all()
            data['result'] = json.loads(serializers.serialize('json',res))
            #序列化信息
            url = addr + '/'+ r.DisasterType + '/' + dataType.__name__
            data['final_url'] = url
            data['is_succeed'] = 'true'
        else:
            data['is_succeed'] = 'false'
            data['reason'] = 'DataType code not exists!'
        #完成请求
        result.status = '1'
        result.save()
    else:
        data['is_succeed'] = 'false'
        data['reason'] = 'Request not exists!'
    return JsonResponse(data)

def import_json_data(url, test_disaster):
    #  用字典的格式存储测试的输入的json数据
    #  将字典格式转化为字符串
    json_str = json.dumps(test_disaster)

    #  将数据写入json文件中
    new_disaster = json.loads(json_str)
    with open(url,  "w") as f:
        json.dump(new_disaster,  f)
    return

# json文件写入数据库表
def read_json_data(url):
    with open(url,  'r') as data:
        parsed_json = json.load(data)
    for item in parsed_json:
        if '111' == item['id'][12:15]:
            disaster = models.DeathStatics.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                number = item['number'],
                reporting_unit = item['reporting_unit']
            )
            disaster.save()
        elif '112' == item['id'][12:15]:
            disaster = models.InjuredStatics.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                number = item['number'],
                reporting_unit = item['reporting_unit']
            )
        elif '113' == item['id'][12:15]:
            disaster = models.MissingStatics.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                number = item['number'],
                reporting_unit = item['reporting_unit']
            )


        elif '221' == item['id'][12:15]:
            disaster = models.CivilStructure.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                basically_intact_square = item['basically_intact_square'],
                damaged_square = item['damaged_square'],
                destroyed_square = item['destroyed_square'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '222' == item['id'][12:15]:
            disaster = models.BrickwoodStructure.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                basically_intact_square = item['basically_intact_square'],
                damaged_square = item['damaged_square'],
                destroyed_square = item['destroyed_square'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '223' == item['id'][12:15]:
            disaster = models.MasonryStructure.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                basically_intact_square = item['basically_intact_square'],
                damaged_square = item['damaged_square'],
                destroyed_square = item['destroyed_square'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '224' == item['id'][12:15]:
            disaster = models.FrameworkStructure.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                basically_intact_square = item['basically_intact_square'],
                damaged_square = item['damaged_square'],
                destroyed_square = item['destroyed_square'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '225' == item['id'][12:15]:
            disaster = models.OtherStructure.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                basically_intact_square = item['basically_intact_square'],
                damaged_square = item['damaged_square'],
                destroyed_square = item['destroyed_square'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )


        elif '336' == item['id'][12:15]:
            disaster = models.CommDisaster.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                type = item['type'],
                grade = item['grade'],
                picture = item['picture'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '331' == item['id'][12:15]:
            disaster = models.TrafficDisaster.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                type = item['type'],
                grade = item['grade'],
                picture = item['picture'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '332' == item['id'][12:15]:
            disaster = models.WaterDisaster.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                type = item['type'],
                grade = item['grade'],
                picture = item['picture'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '333' == item['id'][12:15]:
            disaster = models.OilDisaster.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                type = item['type'],
                grade = item['grade'],
                picture = item['picture'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '334' == item['id'][12:15]:
            disaster = models.GasDisaster.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                type = item['type'],
                grade = item['grade'],
                picture = item['picture'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '335' == item['id'][12:15]:
            disaster = models.PowerDisaster.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                type = item['type'],
                grade = item['grade'],
                picture = item['picture'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )
        elif '337' == item['id'][12:15]:
            disaster = models.IrrigationDisaster.objects.create(
                id = item['id'], 
                date = item['date'],
                location = item['location'],
                type = item['type'],
                grade = item['grade'],
                picture = item['picture'],
                note = item['note'],
                reporting_unit = item['reporting_unit']
            )


        elif '441' == item['id'][12:15]:
            disaster = models.CollapseRecord.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                type = item['type'],
                status = item['status'],
                note = item['note'],
                picture = item.picture['picture'],
                reporting_unit = item['reporting_unit']
            )
        elif '442' == item['id'][12:15]:
            disaster = models.LandslideRecord.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                type = item['type'],
                status = item['status'],
                note = item['note'],
                picture = item.picture['picture'],
                reporting_unit = item['reporting_unit']
            )
        elif '443' == item['id'][12:15]:
            disaster = models.DebrisRecord.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                type = item['type'],
                status = item['status'],
                note = item['note'],
                picture = item.picture['picture'],
                reporting_unit = item['reporting_unit']
            )
        elif '444' == item['id'][12:15]:
            disaster = models.KarstRecord.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                type = item['type'],
                status = item['status'],
                note = item['note'],
                picture = item.picture['picture'],
                reporting_unit = item['reporting_unit']
            )
        elif '445' == item['id'][12:15]:
            disaster = models.CrackRecord.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                type = item['type'],
                status = item['status'],
                note = item['note'],
                picture = item.picture['picture'],
                reporting_unit = item['reporting_unit']
            )
        elif '446' == item['id'][12:15]:
            disaster = models.SettlementRecord.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                type = item['type'],
                status = item['status'],
                note = item['note'],
                picture = item.picture['picture'],
                reporting_unit = item['reporting_unit']
            )
        elif '447' == item['id'][12:15]:
            disaster = models.OtherRecord.objects.create(
                id = item['id'], 
                location = item['location'],
                date = item['date'],
                type = item['type'],
                status = item['status'],
                note = item['note'],
                picture = item.picture['picture'],
                reporting_unit = item['reporting_unit']
            )
        elif '551' == item['id'][12:15]:
            disaster = models.Disasterinfo.objects.create(
                id = item['id'],
                date = item['date'],
                location = item['location'],
                longtitude = item['longtitude'],
                latitude = item['latitude'],
                depth = item['depth'],
                magnitude = item['magnitude'],
                picture = item['picture'],
                reporting_unit = item['reporting_unit']
            )

    # disaster = CommDisaster()
    # json_data = open(url)
    # json_load = json.load(json_data)

    # with open(url,  'r') as data:
    #     parsed_json = json.load(data)
    # return parsed_json


def insert_DeathStatics(request):
    d_statics = DeathStatics()
    # 创建对象
    d_statics.id = request.POST.get('id')
    d_statics.location = request.POST.get('location')
    d_statics.date = request.POST.get('date')
    d_statics.number = request.POST.get('number')
    d_statics.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据
    
    # 为前端返回是否成功的标识
    try:
        data = DeathStatics.objects.filter(id=d_statics.id)
        if data.exists():
            data.delete()
        d_statics.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_DeathStatics')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_DeathStatics(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(DeathStatics,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_DeathStatics')


def insert_InjuredStatics(request):
    # 创建对象
    i_statics = InjuredStatics()
    i_statics.id = request.POST.get('id')
    i_statics.location = request.POST.get('location')
    i_statics.date = request.POST.get('date')
    i_statics.number = request.POST.get('number')
    i_statics.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = InjuredStatics.objects.filter(id=i_statics.id)
        if data.exists():
            data.delete()
        i_statics.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_InjuredStatics')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_InjuredStatics(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(InjuredStatics,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_InjuredStatics')

def insert_MissingStatics(request):
    m_statics = MissingStatics()
    m_statics.id = request.POST.get('id')
    m_statics.location = request.POST.get('location')
    m_statics.date = request.POST.get('date')
    m_statics.number = request.POST.get('number')
    m_statics.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    try:
        data = InjuredStatics.objects.filter(id=m_statics.id)
        if data.exists():
            data.delete()
        m_statics.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_MissingStatics')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_MissingStatics(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(MissingStatics,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_MissingStatics')

def insert_CivilStructure(request):
    c_structure = CivilStructure()
    # 创建对象
    c_structure.id = request.POST.get('id')
    c_structure.date = request.POST.get('date')
    c_structure.location = request.POST.get('location')
    c_structure.basically_intact_square = request.POST.get('basically_intact_square')
    c_structure.damaged_square = request.POST.get('damaged_square')
    c_structure.destroyed_square = request.POST.get('destroyed_square')
    c_structure.note = request.POST.get('note')
    c_structure.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据
    #  为前端返回是否成功的标识
    try:
        data = InjuredStatics.objects.filter(id=c_structure.id)
        if data.exists():
            data.delete()
        c_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_CivilStructure')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_CivilStructure(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(CivilStructure,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_CivilStructure')

def insert_BrickwoodStructure(request):
    b_structure = BrickwoodStructure()
    b_structure.id = request.POST.get('id')
    b_structure.date = request.POST.get('date')
    b_structure.location = request.POST.get('location')
    b_structure.basically_intact_square = request.POST.get('basically_intact_square')
    b_structure.damaged_square = request.POST.get('damaged_square')
    b_structure.destroyed_square = request.POST.get('destroyed_square')
    b_structure.note = request.POST.get('note')
    b_structure.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = BrickwoodStructure.objects.filter(id=b_structure.id)
        if data.exists():
            data.delete()
        b_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_BrickwoodStructure')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_BrickwoodStructure(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(BrickwoodStructure,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_BrickwoodStructure')

def insert_MasonryStructure(request):
    m_structure = MasonryStructure()
    m_structure.id = request.POST.get('id')
    m_structure.date = request.POST.get('date')
    m_structure.location = request.POST.get('location')
    m_structure.basically_intact_square = request.POST.get('basically_intact_square')
    m_structure.slight_damaged_square = request.POST.get('slight_damaged_square')
    m_structure.moderate_damaged_square = request.POST.get('moderate_damaged_square')
    m_structure.serious_damaged_square = request.POST.get('serious_damaged_square')
    m_structure.destroyed_square = request.POST.get('destroyed_square')
    m_structure.note = request.POST.get('note')
    m_structure.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = MasonryStructure.objects.filter(id=m_structure.id)
        if data.exists():
            data.delete()
        m_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_MasonryStructure')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_MasonryStructure(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(MasonryStructure,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_MasonryStructure')

def insert_FrameworkStructure(request):
    f_structure = FrameworkStructure()
    f_structure.id = request.POST.get('id')
    f_structure.date = request.POST.get('date')
    f_structure.location = request.POST.get('location')
    f_structure.basically_intact_square = request.POST.get('basically_intact_square')
    f_structure.slight_damaged_square = request.POST.get('slight_damaged_square')
    f_structure.moderate_damaged_square = request.POST.get('moderate_damaged_square')
    f_structure.serious_damaged_square = request.POST.get('serious_damaged_square')
    f_structure.destroyed_square = request.POST.get('destroyed_square')
    f_structure.note = request.POST.get('note')
    f_structure.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = FrameworkStructure.objects.filter(id=f_structure.id)
        if data.exists():
            data.delete()
        f_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_FrameworkStructure')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_FrameworkStructure(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(FrameworkStructure,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_FrameworkStructure')

def insert_OtherStructure(request):
    o_structure = OtherStructure()
    o_structure.id = request.POST.get('id')
    o_structure.date = request.POST.get('date')
    o_structure.location = request.POST.get('location')
    o_structure.basically_intact_square = request.POST.get('basically_intact_square')
    o_structure.slight_damaged_square = request.POST.get('slight_damaged_square')
    o_structure.moderate_damaged_square = request.POST.get('moderate_damaged_square')
    o_structure.serious_damaged_square = request.POST.get('serious_damaged_square')
    o_structure.destroyed_square = request.POST.get('destroyed_square')
    o_structure.note = request.POST.get('note')
    o_structure.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = OtherStructure.objects.filter(id=o_structure.id)
        if data.exists():
            data.delete()
        o_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_OtherStructure')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_OtherStructure(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(OtherStructure,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_OtherStructure')

def insert_CommDisaster(request):
    disaster = CommDisaster()
    # 创建对象
    disaster.id = request.POST.get('id')
    disaster.date = request.POST.get('date')
    disaster.location = request.POST.get('location')
    disaster.type = request.POST.get('type')
    disaster.data = request.POST.get('data')
    disaster.structure = request.POST.get('structure')
    disaster.square = request.POST.get('square')
    disaster.note = request.POST.get('note')
    disaster.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据
    # 为前端返回是否成功的标识
    try:
        data = CommDisaster.objects.filter(id=disaster.id)
        if data.exists():
            data.delete()
        disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        #  没有save成功的时候返回false失败
    return redirect('details_CommDisaster')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_CommDisaster(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(CommDisaster,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_CommDisaster')

def insert_TrafficDisaster(request):
    t_disaster = TrafficDisaster()
    # 创建对象
    t_disaster.id = request.POST.get('id')
    t_disaster.date = request.POST.get('date')
    t_disaster.location = request.POST.get('location')
    t_disaster.type = request.POST.get('type')
    t_disaster.grade = request.POST.get('grade')
    t_disaster.note = request.POST.get('note')
    t_disaster.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = TrafficDisaster.objects.filter(id=t_disaster.id)
        if data.exists():
            data.delete()
        t_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_TrafficDisaster')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_TrafficDisaster(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(TrafficDisaster,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_TrafficDisaster')

def insert_WaterDisaster(request):
    w_disaster = WaterDisaster()
    # 创建对象
    w_disaster.id = request.POST.get('id')
    w_disaster.date = request.POST.get('date')
    w_disaster.location = request.POST.get('location')
    w_disaster.type = request.POST.get('type')
    w_disaster.grade = request.POST.get('grade')
    w_disaster.note = request.POST.get('note')
    w_disaster.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = WaterDisaster.objects.filter(id=w_disaster.id)
        if data.exists():
            data.delete()
        w_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_WaterDisaster')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_WaterDisaster(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(WaterDisaster,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_WaterDisaster')

def insert_PowerDisaster(request):
    p_disaster = PowerDisaster()
    # 创建对象
    p_disaster.id = request.POST.get('id')
    p_disaster.date = request.POST.get('date')
    p_disaster.location = request.POST.get('location')
    p_disaster.type = request.POST.get('type')
    p_disaster.grade = request.POST.get('grade')
    p_disaster.note = request.POST.get('note')
    p_disaster.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = PowerDisaster.objects.filter(id=p_disaster.id)
        if data.exists():
            data.delete()
        # 成功save的时候返回成功
        p_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_PowerDisaster')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_PowerDisaster(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(PowerDisaster,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_PowerDisaster')

def insert_OilDisaster(request):
    o_disaster = OilDisaster()
    # 创建对象
    o_disaster.id = request.POST.get('id')
    o_disaster.date = request.POST.get('date')
    o_disaster.location = request.POST.get('location')
    o_disaster.type = request.POST.get('type')
    o_disaster.grade = request.POST.get('grade')
    o_disaster.note = request.POST.get('note')
    o_disaster.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = PowerDisaster.objects.filter(id=o_disaster.id)
        if data.exists():
            data.delete()
        o_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_OilDisaster')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_OilDisaster(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(OilDisaster,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_OilDisaster')

def insert_IrrigationDisaster(request):
    i_disaster = IrrigationDisaster()
    # 创建对象
    i_disaster.id = request.POST.get('id')
    i_disaster.date = request.POST.get('date')
    i_disaster.location = request.POST.get('location')
    i_disaster.type = request.POST.get('type')
    i_disaster.grade = request.POST.get('grade')
    i_disaster.note = request.POST.get('note')
    i_disaster.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = IrrigationDisaster.objects.filter(id=i_disaster.id)
        if data.exists():
            data.delete()
        i_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_IrrigationDisaster')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_IrrigationDisaster(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(IrrigationDisaster,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_IrrigationDisaster')

def insert_GasDisaster(request):
    g_disaster = GasDisaster()
    # 创建对象
    g_disaster.id = request.POST.get('id')
    g_disaster.date = request.POST.get('date')
    g_disaster.location = request.POST.get('location')
    g_disaster.type = request.POST.get('type')
    g_disaster.grade = request.POST.get('grade')
    g_disaster.note = request.POST.get('note')
    g_disaster.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    # 获取数据

    # 为前端返回是否成功的标识
    try:
        data = GasDisaster.objects.filter(id=g_disaster.id)
        if data.exists():
            data.delete()
        g_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_GasDisaster')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_GasDisaster(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(GasDisaster,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_GasDisaster')

#  CollapseRecord
def insert_CollapseRecord(request):
    c_record = CollapseRecord()
    c_record.id = request.POST.get('id')
    c_record.location = request.POST.get('location')
    c_record.date = request.POST.get('date')
    c_record.type = request.POST.get('type')
    c_record.status = request.POST.get('status')
    c_record.note = request.POST.get('note')
    #  c_record.picture = cv2.imread('earthquake.jpg')
    c_record.picture = request.POST.get('picture')
    c_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')

    # 为前端返回是否成功的标识
    try:
        data = CollapseRecord.objects.filter(id=c_record.id)
        if data.exists():
            data.delete()
        c_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_CollapseRecord')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_CollapseRecord(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(CollapseRecord,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_CollapseRecord')

#  CollapseRecord
def insert_LandslideRecord(request):
    l_record = LandslideRecord()
    l_record.id = request.POST.get('id')
    l_record.location = request.POST.get('location')
    l_record.date = request.POST.get('date')
    l_record.type = request.POST.get('type')
    l_record.status = request.POST.get('status')
    l_record.note = request.POST.get('note')
    #  c_record.picture = cv2.imread('earthquake.jpg')
    l_record.picture = request.POST.get('picture')
    l_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')

    # 为前端返回是否成功的标识
    try:
        data = LandslideRecord.objects.filter(id=l_record.id)
        if data.exists():
            data.delete()
        l_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_LandslideRecord')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_LandslideRecord(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(LandslideRecord,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_LandslideRecord')

#  CollapseRecord
def insert_DebrisRecord(request):
    d_record = DebrisRecord()
    d_record.id = request.POST.get('id')
    d_record.location = request.POST.get('location')
    d_record.date = request.POST.get('date')
    d_record.type = request.POST.get('type')
    d_record.status = request.POST.get('status')
    d_record.note = request.POST.get('note')
    #  c_record.picture = cv2.imread('earthquake.jpg')
    d_record.picture = request.POST.get('picture')
    d_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')

    # 为前端返回是否成功的标识
    try:
        data = DebrisRecord.objects.filter(id=d_record.id)
        if data.exists():
            data.delete()
        d_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_DebrisRecord')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_DebrisRecord(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(DebrisRecord,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_DebrisRecord')

# KarstRecord
def insert_KarstRecord(request):
    k_record = KarstRecord()
    k_record.id = request.POST.get('id')
    k_record.location = request.POST.get('location')
    k_record.date = request.POST.get('date')
    k_record.type = request.POST.get('type')
    k_record.status = request.POST.get('status')
    k_record.note = request.POST.get('note')
    #  c_record.picture = cv2.imread('earthquake.jpg')
    k_record.picture = request.POST.get('picture')
    k_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')

    # 为前端返回是否成功的标识
    try:
        data = KarstRecord.objects.filter(id=k_record.id)
        if data.exists():
            data.delete()
        k_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_KarstRecord')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_KarstRecord(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(KarstRecord,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_KarstRecord')

# KarstRecord
def insert_CrackRecord(request):
    c_record = CrackRecord()
    c_record.id = request.POST.get('id')
    c_record.location = request.POST.get('location')
    c_record.date = request.POST.get('date')
    c_record.type = request.POST.get('type')
    c_record.status = request.POST.get('status')
    c_record.note = request.POST.get('note')
    #  c_record.picture = cv2.imread('earthquake.jpg')
    c_record.picture = request.POST.get('picture')
    c_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')

    # 为前端返回是否成功的标识
    try:
        data = CrackRecord.objects.filter(id=c_record.id)
        if data.exists():
            data.delete()
        c_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_CrackRecord')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_CrackRecord(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(CrackRecord,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_CrackRecord')

# KarstRecord
def insert_SettlementRecord(request):
    s_record = SettlementRecord()
    s_record.id = request.POST.get('id')
    s_record.location = request.POST.get('location')
    s_record.date = request.POST.get('date')
    s_record.type = request.POST.get('type')
    s_record.status = request.POST.get('status')
    s_record.note = request.POST.get('note')
    #  c_record.picture = cv2.imread('earthquake.jpg')
    s_record.picture = request.POST.get('picture')
    s_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')

    # 为前端返回是否成功的标识
    try:
        data = SettlementRecord.objects.filter(id=s_record.id)
        if data.exists():
            data.delete()
        s_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_SettlementRecord')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_SettlementRecord(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(SettlementRecord,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_SettlementRecord')

# KarstRecord
def insert_OtherRecord(request):
    o_record = OtherRecord()
    o_record.id = request.POST.get('id')
    o_record.location = request.POST.get('location')
    o_record.date = request.POST.get('date')
    o_record.type = request.POST.get('type')
    o_record.status = request.POST.get('status')
    o_record.note = request.POST.get('note')
    #  c_record.picture = cv2.imread('earthquake.jpg')
    o_record.picture = request.POST.get('picture')
    o_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')

    # 为前端返回是否成功的标识
    try:
        data = OtherRecord.objects.filter(id=o_record.id)
        if data.exists():
            data.delete()
        o_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_OtherRecord')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_OtherRecord(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(OtherRecord,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_OtherRecord')

#  Disasterinfo
def insert_DisasterInfo(request):
    d_info = DisasterInfo()
    d_info.id = request.POST.get('id')
    d_info.date = request.POST.get('date')
    d_info.location = request.POST.get('location')
    d_info.longtitude = request.POST.get('longtitude')
    d_info.latitude = request.POST.get('latitude')
    d_info.depth = request.POST.get('depth')
    d_info.magnitude = request.POST.get('magnitude')
    #  d_prediction.picture = '0000'
    d_info.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    try:
        data = DisasterInfo.objects.filter(id=d_info.id)
        if data.exists():
            data.delete()
        d_info.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_DisasterInfo')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_DisasterInfo(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(DisasterInfo,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_DisasterInfo')

#  DisasterPrediction
def insert_DisatserPrediction(request):
    d_prediction = DisatserPrediction()
    d_prediction.id = request.POST.get('id')
    d_prediction.date = request.POST.get('date')
    d_prediction.location = request.POST.get('location')
    d_prediction.longtitude = request.POST.get('longtitude')
    d_prediction.latitude = request.POST.get('latitude')
    d_prediction.depth = request.POST.get('depth')
    d_prediction.magnitude = request.POST.get('magnitude')
    d_prediction.intensity = request.POST.get('intensity')
    d_prediction.type = request.POST.get('type')
    d_prediction.note = request.POST.get('note')
    #  d_prediction.picture = '0000'
    d_prediction.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    try:
        data = DisatserPrediction.objects.filter(id=d_prediction.id)
        if data.exists():
            data.delete()
        d_prediction.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_DisatserPrediction')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_DisatserPrediction(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(DisatserPrediction,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_DisatserPrediction')

#  DisasterPrediction
def insert_DisasterRequest(request):
    d_request = DisasterRequest()
    d_request.date = request.POST.get('date')
    d_request.disasterType = request.POST.get('disasterType')
    d_request.o_URL = request.POST.get('o_URL')
    d_request.requestunit = request.POST.get('requestunit')
    d_request.status = '0'
    #  d_prediction.picture = '0000'
    try:
        d_request.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except Exception:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return redirect('details_DisasterRequest')
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def del_DisasterRequest(request):
    id = request.GET.get('id')
    try:
        data = get_object_or_404(DisasterRequest,id=id)
        data.delete()
        is_succeed = {"is_succeed": "true"}
    except Exception:
        is_succeed = {"is_succeed": "false"}
    return redirect('details_DisasterRequest')

def index_20200504(request):
    return render(request, 'index_20200504.html', )

def index_20200514(request):
    return render(request, 'index_20200514.html', )

def index_20200519(request):
    return render(request, 'index_20200519.html', )

def details_xmxx(request):
    DeathStatics_records = DeathStatics.objects.all()
    MissingStatics_records = MissingStatics.objects.all()
    CivilStructure_records = CivilStructure.objects.all()
    MasonryStructure_records = MasonryStructure.objects.all()
    CommDisaster_records = CommDisaster.objects.all()
    TrafficDisaster_records = TrafficDisaster.objects.all()
    CollapseRecord_records = CollapseRecord.objects.all()
    LandslideRecord_records = LandslideRecord.objects.all()
    DisasterInfo_records = DisasterInfo.objects.all()
    DisatserPrediction_records = DisatserPrediction.objects.all()

    return render(request, 'details_xmxx.html', 
    {
        'DeathStatics_records': DeathStatics_records, 
        'MissingStatics_records': MissingStatics_records, 
        'CivilStructure_records': CivilStructure_records, 
        'MasonryStructure_records': MasonryStructure_records, 
        'CommDisaster_records': CommDisaster_records, 
        'TrafficDisaster_records': TrafficDisaster_records, 
        'CollapseRecord_records': CollapseRecord_records, 
        'LandslideRecord_records': LandslideRecord_records, 
        'DisasterInfo_records': DisasterInfo_records, 
        'DisatserPrediction_records': DisatserPrediction_records, 
    }
    )

def details_DeathStatics(request):
    DeathStatics_records = DeathStatics.objects.all()
    MissingStatics_records = MissingStatics.objects.all()
    CivilStructure_records = CivilStructure.objects.all()
    MasonryStructure_records = MasonryStructure.objects.all()
    CommDisaster_records = CommDisaster.objects.all()
    TrafficDisaster_records = TrafficDisaster.objects.all()
    CollapseRecord_records = CollapseRecord.objects.all()
    LandslideRecord_records = LandslideRecord.objects.all()
    DisasterInfo_records = DisasterInfo.objects.all()
    DisatserPrediction_records = DisatserPrediction.objects.all()

    return render(request, 'details_DeathStatics.html', 
    {
        'DeathStatics_records': DeathStatics_records, 
        'MissingStatics_records': MissingStatics_records, 
        'CivilStructure_records': CivilStructure_records, 
        'MasonryStructure_records': MasonryStructure_records, 
        'CommDisaster_records': CommDisaster_records, 
        'TrafficDisaster_records': TrafficDisaster_records, 
        'CollapseRecord_records': CollapseRecord_records, 
        'LandslideRecord_records': LandslideRecord_records, 
        'DisasterInfo_records': DisasterInfo_records, 
        'DisatserPrediction_records': DisatserPrediction_records, 
    }
    )

def details_InjuredStatics(request):
    InjuredStatics_records = InjuredStatics.objects.all()

    return render(request, 'details_InjuredStatics.html', 
    {
        'InjuredStatics_records': InjuredStatics_records, 
    }
    )

def details_MissingStatics(request):
    MissingStatics_records = MissingStatics.objects.all()

    return render(request, 'details_MissingStatics.html', 
    {
        'MissingStatics_records': MissingStatics_records, 
    }
    )

def details_CivilStructure(request):
    CivilStructure_records = CivilStructure.objects.all()

    return render(request, 'details_CivilStructure.html', 
    {
        'CivilStructure_records': CivilStructure_records, 
    }
    )

def details_BrickwoodStructure(request):
    BrickwoodStructure_records = BrickwoodStructure.objects.all()

    return render(request, 'details_BrickwoodStructure.html', 
    {
        'BrickwoodStructure_records': BrickwoodStructure_records, 
    }
    )

def details_MasonryStructure(request):
    MasonryStructure_records = MasonryStructure.objects.all()

    return render(request, 'details_MasonryStructure.html', 
    {
        'MasonryStructure_records': MasonryStructure_records, 
    }
    )

def details_FrameworkStructure(request):
    FrameworkStructure_records = FrameworkStructure.objects.all()

    return render(request, 'details_FrameworkStructure.html', 
    {
        'FrameworkStructure_records': FrameworkStructure_records, 
    }
    )

def details_OtherStructure(request):
    OtherStructure_records = OtherStructure.objects.all()

    return render(request, 'details_OtherStructure.html', 
    {
        'OtherStructure_records': OtherStructure_records, 
    }
    )

def details_CommDisaster(request):
    CommDisaster_records = CommDisaster.objects.all()

    return render(request, 'details_CommDisaster.html', 
    {
        'CommDisaster_records': CommDisaster_records, 
    }
    )

def details_TrafficDisaster(request):
    TrafficDisaster_records = TrafficDisaster.objects.all()

    return render(request, 'details_TrafficDisaster.html', 
    {
        'TrafficDisaster_records': TrafficDisaster_records, 
    }
    )

def details_WaterDisaster(request):
    WaterDisaster_records = WaterDisaster.objects.all()

    return render(request, 'details_WaterDisaster.html', 
    {
        'WaterDisaster_records': WaterDisaster_records, 
    }
    )

def details_OilDisaster(request):
    OilDisaster_records = OilDisaster.objects.all()

    return render(request, 'details_OilDisaster.html', 
    {
        'OilDisaster_records': OilDisaster_records, 
    }
    )

def details_GasDisaster(request):
    GasDisaster_records = GasDisaster.objects.all()

    return render(request, 'details_GasDisaster.html', 
    {
        'GasDisaster_records': GasDisaster_records, 
    }
    )

def details_PowerDisaster(request):
    PowerDisaster_records = PowerDisaster.objects.all()

    return render(request, 'details_PowerDisaster.html', 
    {
        'PowerDisaster_records': PowerDisaster_records, 
    }
    )

def details_IrrigationDisaster(request):
    IrrigationDisaster_records = IrrigationDisaster.objects.all()

    return render(request, 'details_IrrigationDisaster.html', 
    {
        'IrrigationDisaster_records': IrrigationDisaster_records, 
    }
    )

def details_CollapseRecord(request):
    CollapseRecord_records = CollapseRecord.objects.all()

    return render(request, 'details_CollapseRecord.html', 
    {
        'CollapseRecord_records': CollapseRecord_records, 
    }
    )

def details_LandslideRecord(request):
    LandslideRecord_records = LandslideRecord.objects.all()

    return render(request, 'details_LandslideRecord.html', 
    {
        'LandslideRecord_records': LandslideRecord_records, 
    }
    )

def details_DebrisRecord(request):
    DebrisRecord_records = DebrisRecord.objects.all()

    return render(request, 'details_DebrisRecord.html', 
    {
        'DebrisRecord_records': DebrisRecord_records, 
    }
    )

def details_KarstRecord(request):
    KarstRecord_records = KarstRecord.objects.all()

    return render(request, 'details_KarstRecord.html', 
    {
        'KarstRecord_records': KarstRecord_records, 
    }
    )

def details_CrackRecord(request):
    CrackRecord_records = CrackRecord.objects.all()

    return render(request, 'details_CrackRecord.html', 
    {
        'CrackRecord_records': CrackRecord_records, 
    }
    )

def details_SettlementRecord(request):
    SettlementRecord_records = SettlementRecord.objects.all()

    return render(request, 'details_SettlementRecord.html', 
    {
        'SettlementRecord_records': SettlementRecord_records, 
    }
    )

def details_OtherRecord(request):
    OtherRecord_records = OtherRecord.objects.all()

    return render(request, 'details_OtherRecord.html', 
    {
        'OtherRecord_records': OtherRecord_records, 
    }
    )

def details_DisasterInfo(request):
    DisasterInfo_records = DisasterInfo.objects.all()

    return render(request, 'details_DisasterInfo.html', 
    {
        'DisasterInfo_records': DisasterInfo_records, 
    }
    )

def details_DisatserPrediction(request):
    DisatserPrediction_records = DisatserPrediction.objects.all()

    return render(request, 'details_DisatserPrediction.html', 
    {
        'DisatserPrediction_records': DisatserPrediction_records, 
    }
    )

def details_DisasterRequest(request):
    DisasterRequest_records = DisasterRequest.objects.all()

    return render(request, 'details_DisasterRequest.html', 
    {
        'DisasterRequest_records': DisasterRequest_records, 
    }
    )


def index(request):
    return render(request, 'index.html', )


# 测试灾情编码的映射
def id_mapping(get_value):

    # 基础地理信息编码
    key_list01 = []
    value_list01 = []
    adminiDivisionsDict = { '江苏省南京市玄武区新街口街道大石桥社区':'010101002004',  
                            '广东省广州市越秀区白云街道广九社区':'020101007005',  
                            '江苏省苏州市吴中区长桥街道宝带桥社区':'010201001001'}

    for key, value in adminiDivisionsDict.items():
        key_list01.append(key)
        value_list01.append(value)

    get_value01 = get_value[0:12]
    if get_value01 in value_list01:
        get_value_index = value_list01.index(get_value01)
        print("基础地理信息：%s" %key_list01[get_value_index])
    else:
        print("基础地理信息：%s不存在" %get_value01)


    # 灾情信息编码
    key_list02 = []
    value_list02 = []
    disasterInfo = {'人员伤亡及失踪-死亡':'111', 
                    '房屋破坏-土木':'221', 
                    '生命线工程灾情-通信':'336', 
                    '次生灾害-崩塌':'441', 
                    '震情-灾情预测':'552'}

    for key, value in disasterInfo.items():
        key_list02.append(key)
        value_list02.append(value)


    get_value02 = get_value[12:15]
    if get_value02 in value_list02:
        get_value_index = value_list02.index(get_value02)
        print("灾情信息：%s" %key_list02[get_value_index])
    else:
        print("灾情信息：%s不存在" %get_value02)


    # 多源异构数据编码
    key_list03 = []
    value_list03 = []
    originInfo = {'业务报送数据-公网':'1101', 
                  '泛在感知数据-通信网':'2202', 
                  '舆情感知数据-微博':'3301', 
                  '承载体基础数据-川滇':'4401'}

    for key, value in originInfo.items():
        key_list03.append(key)
        value_list03.append(value)


    get_value03 = get_value[15:19]
    if get_value03 in value_list03:
        get_value_index = value_list03.index(get_value03)
        print("多源异构信息：%s" %key_list03[get_value_index])
    else:
        print("多源异构信息：%s不存在" %get_value03)

