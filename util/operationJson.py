# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
import json
class operationjson():
    def __init__(self,filename=None):
        if filename:
            self.filename = filename
        else:
            self.filename = r'D:\PyCharmProject\api-test-python3\data\testcase.json'
        self.jsondata = self.get_json_data()
    def get_json_data(self):
        with open(self.filename,'r') as f:
            jsons = json.load(f)  #转字典
            #jsons = f.read()  #原输出json字符串
            return jsons
    def get_josn_key_data(self,key):
        value = self.jsondata[key]
        return value
if __name__ == '__main__':
    js = operationjson()
    jsons = js.get_json_data()
    value = js.get_josn_key_data('login')
    print(jsons)
    print(type(jsons))
    print(value)
    print(type(value))