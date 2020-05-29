# -*- coding: utf-8 -*-
"""
Created on 2020-01-08
@author: panzhaochao
"""
import requests
import json
from util.getRequestsdata import getresdata
class sendrequests():
    def get_main(self, url, params= None,headers = None):  # get请求
        try:
            res = requests.get(url, params=params, headers=headers)
            res.encoding = 'UTF-8'
            results = json.loads(res.text)
            return json.dumps(results, indent=2)
        except Exception as e:
            return ('发送get请求错误：%s'%e)

    def post_main(self, url, params= None,headers = None): # post请求
        try:
            if headers == '':
                res = requests.post(url, params=params)
            else:
                res = requests.post(url,json=params,headers=headers)
            res.encoding = 'UTF-8'
            results = json.loads(res.text)
            return json.dumps(results, indent=2)
        except Exception as e:
            return ('发送psot请求错误：%s'%e)

    def del_main(self, url, params= None,headers = None): #delete请求
        try:
            res = requests.delete(url, params=params,headers=headers)
            res.encoding = 'UTF-8'
            results = json.loads(res.text)
            return json.dumps(results, indent=2)
        except Exception as e:
            return ('发送delete请求错误：%s'%e)

    def put_main(self, url, params= None): #put请求
        try:
            res = requests.put(url, params=params)
            res.encoding = 'UTF-8'
            results = json.loads(res.text)
            return json.dumps(results, indent=2)
        except Exception as e:
            return ('发送put请求错误：%s'%e)
    def send_request(self,method,url,params=None,headers=None):
        res = None
        methods = method.upper()
        if methods == 'GET':
            res = sendrequests().get_main(url,params,headers)
        elif methods == 'POST':
            res = sendrequests().post_main(url,params,headers)
        elif methods == 'DELETE':
            res = sendrequests().del_main(url,params)
        elif methods == 'PUT':
            res = sendrequests().put_main(url,params)
        return res