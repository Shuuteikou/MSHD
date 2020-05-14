from django.shortcuts import render
from data_resolver.models import CommDisaster

import json
# Create your views here.
def read_json_data(url):
    disaster = CommDisaster()
    json_data = open(url)
    json_load = json.load(json_data)

    with open(url, 'r') as data:
        parsed_json = json.load(data)
    return parsed_json


def import_json_data(url,test_disaster):
    # 用字典的格式存储测试的输入的json数据
    # 将字典格式转化为字符串
    json_str = json.dumps(test_disaster)

    # 将数据写入json文件中
    new_disaster = json.loads(json_str)
    with open(url, "w") as f:
        json.dump(new_disaster, f)
    return