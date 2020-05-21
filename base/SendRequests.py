# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
import requests
import json
from util.getRequestsdata import getresdata
class sendrequests():
    def get_main(self, url, params= None,headers = None):  # get请求
        res = requests.get(url, params=params, headers=headers)
        res.encoding = 'UTF-8'
        results = json.loads(res.text)
        return json.dumps(results, indent=2)

    def post_main(self, url, params= None,headers = None): # post请求
        if headers == '':
            res = requests.post(url, params=params)
        else:
            res = requests.post(url,json=params,headers=headers)
        res.encoding = 'UTF-8'
        results = json.loads(res.text)
        return json.dumps(results, indent=2)
    def del_main(self, url, params= None,headers = None): #delete请求
        res = requests.delete(url, params=params,headers=headers)
        res.encoding = 'UTF-8'
        results = json.loads(res.text)
        return json.dumps(results, indent=2)

    def put_main(self, url, params= None): #put请求
        res = requests.put(url, params=params)
        res.encoding = 'UTF-8'
        results = json.loads(res.text)
        return json.dumps(results, indent=2)
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
if __name__ == '__main__':
    url = 'http://192.168.7.242:8380/rest/app/user/login'
    params = {'appKey':'xyhqfhnlqqvvotdipz','uname':'test20200217','deviceId':'bs0126','pwd':'123123'}
    # url = 'http://127.0.0.1:8380//login'
    # params = {'name':'panzc','pwd':'123123'}
#     url = 'http://192.168.7.242:8380/rest/service/add/group'
#     params = {
# 	"name":"123",
# 	"nodes":[
# 		{
# 		"seq":"11",
# 		"lng":"11",
# 		"lat":"11",
# 		"height":"11"
# 		},
# 		{
# 		"seq":1993,
# 		"lng":23.4043,
# 		"lat":113.4043,
# 		"height":3.4043
# 			}
# 	]
#
# }
    headers = {'Content-Type': 'application/json'}
    run = sendrequests()
    method = 'get'
    res = run.send_request(method,url,params)
    print(res)