#!/usr/bin/env python
# -*- encoding:utf-8 -*-

from django.shortcuts import render

#  人员
from .models import DeathStatics,MissingStatics,InjuredStatics
#  房屋
from .models import CivilStructure, MasonryStructure, BrickwoodStructure, FrameworkStructure,OtherStructure
#  生命线
from .models import CommDisaster, TrafficDisaster,WaterDisaster,OilDisaster,GasDisaster,IrrigationDisaster,PowerDisaster
#  次生灾害
from .models import CollapseRecord,LandslideRecord,DebrisRecord,KarstRecord,CrackRecord,SettlementRecord,OtherRecord
#  震情
from .models import DisasterInfo,DisatserPrediction,DisasterRequest

from django.shortcuts import get_object_or_404, render
#  from .models import day,todo


import json

#  Create your views here.
def read_json_data(url):
    disaster = CommDisaster()
    json_data = open(url)
    json_load = json.load(json_data)

    with open(url, 'r') as data:
        parsed_json = json.load(data)
    return parsed_json


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
        
        if d_statics.pk is not None:
            d_statics.delete()
        d_statics.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def insert_InjuredStatics(request):
    d_statics = DeathStatics()
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
        if i_statics.pk is not None:
            i_statics.delete()
        i_statics.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def insert_MissingStatics(request):
    m_statics = MissingStatics()
    m_statics.id = request.POST.get('id')
    m_statics.location = request.POST.get('location')
    m_statics.date = request.POST.get('date')
    m_statics.number = request.POST.get('number')
    m_statics.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    try:
        if m_statics.pk is not None:
            m_statics.delete()
        m_statics.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）


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
        if c_structure.pk is not None:
            c_structure.delete()
        c_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
<<<<<<< HEAD
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）
=======
        #没有save成功的时候返回false失败
    return render(request,'details_DeathStatics.html',is_succeed)
    #render返回deathstatics的页面（这个render的页面之后改成原来的页面）
>>>>>>> 85d8f6d4465133a3458ffe4abf9d5786d95497f0

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
        if b_structure.pk is not None:
            b_structure.delete()
        b_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if m_structure.pk is not None:
            m_structure.delete()
        m_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if f_structure.pk is not None:
            f_structure.delete()
        f_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if o_structure.pk is not None:
            o_structure.delete()
        o_structure.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def insert_CoomDisaster(request):
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
        if disaster.pk is not None:
            disaster.delete()
        disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        #  没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if t_disaster.pk is not None:
            t_disaster.delete()
        t_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if w_disaster.pk is not None:
            w_disaster.delete()
        w_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if p_disaster.pk is not None:
            p_disaster.delete()
        p_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if o_disaster.pk is not None:
            o_disaster.delete()
        o_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）


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
        if i_disaster.pk is not None:
            i_disaster.delete()
        i_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if g_disaster.pk is not None:
            g_disaster.delete()
        g_disaster.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
    c_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    
    # 为前端返回是否成功的标识
    try:
        if c_record.pk is not None:
            c_record.delete()
        c_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
    l_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    
    # 为前端返回是否成功的标识
    try:
        if l_record.pk is not None:
            l_record.delete()
        l_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
    d_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    
    # 为前端返回是否成功的标识
    try:
        if d_record.pk is not None:
            d_record.delete()
        d_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
    k_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    
    # 为前端返回是否成功的标识
    try:
        if k_record.pk is not None:
            k_record.delete()
        k_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
    c_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    
    # 为前端返回是否成功的标识
    try:
        if c_record.pk is not None:
            c_record.delete()
        c_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
    s_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    
    # 为前端返回是否成功的标识
    try:
        if s_record.pk is not None:
            s_record.delete()
        s_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
    o_record.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    
    # 为前端返回是否成功的标识
    try:
        if o_record.pk is not None:
            o_record.delete()
        o_record.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

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
        if d_info.pk is not None:
            d_info.delete()
        d_info.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）


#  DisasterPrediction
def insert_DisasterPrediction(request):
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
        if d_prediction.pk is not None:
            d_prediction.delete()
        d_prediction.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

#  DisasterPrediction
def insert_DisasterRequest(request):
    d_request = DisasterRequest()
    d_request.id = request.POST.get('id')
    d_request.date = request.POST.get('date')
    d_request.disasterType = request.POST.get('disasterType')
    d_request.status = request.POST.get('status')
    #  d_prediction.picture = '0000'
    d_request.reporting_unit = request.POST.get('ms_code') + request.POST.get('reporting_unit')
    try:
        if d_request.pk is not None:
            d_request.delete()
        d_request.save()
        is_succeed = {"is_succeed": "true"}
        # 成功save的时候返回成功
    except:
        is_succeed = {"is_succeed": "false"}
        # 没有save成功的时候返回false失败
    return render(request,'index_20200504.html',is_succeed)
    # render返回deathstatics的页面（这个render的页面之后改成原来的页面）

def index_20200504(request):
    return render(request,'index_20200504.html',)

def index_20200514(request):
    return render(request,'index_20200514.html',)

def index_20200519(request):
    return render(request,'index_20200519.html',)

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

    return render(request,'details_xmxx.html',
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

    return render(request,'details_DeathStatics.html',
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

def index(request):
    return render(request,'index.html',)

def import_json_data(url,test_disaster):
    #  用字典的格式存储测试的输入的json数据
    #  将字典格式转化为字符串
    json_str = json.dumps(test_disaster)

    #  将数据写入json文件中
    new_disaster = json.loads(json_str)
    with open(url, "w") as f:
        json.dump(new_disaster, f)
    return

# 测试灾情编码的映射
def id_mapping(get_value):

    # 基础地理信息编码
    key_list01 = []
    value_list01 = []
    adminiDivisionsDict = { '江苏省南京市玄武区新街口街道大石桥社区':'010101002004', 
                            '广东省广州市越秀区白云街道广九社区':'020101007005', 
                            '江苏省苏州市吴中区长桥街道宝带桥社区':'010201001001'}

    for key,value in adminiDivisionsDict.items():
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

    for key,value in disasterInfo.items():
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

    for key,value in originInfo.items():
        key_list03.append(key)
        value_list03.append(value)


    get_value03 = get_value[15:19]
    if get_value03 in value_list03:
        get_value_index = value_list03.index(get_value03)
        print("多源异构信息：%s" %key_list03[get_value_index])
    else:
        print("多源异构信息：%s不存在" %get_value03)

