# -*- coding: utf-8 -*-
"""
Created on 2020-01-08
@author: panzhaochao
"""
import json
from common.GetConfData import getConfingdata
class operationjson():
    def __init__(self):
        filenamepath = 'filenamepath'
        jsonname = 'jsonname'
        self.filename = getConfingdata().get_conf_data(filenamepath,jsonname)
        self.jsondata = self.get_json_data()
    def get_json_data(self):
        try:
            with open(self.filename,'r') as f:
                jsons = json.load(f)  #转字典
                return jsons
        except Exception as e:
            return ('读取json文件失败：%s'%e)
    def get_josn_key_data(self,key):
        value = self.jsondata[key]
        return value