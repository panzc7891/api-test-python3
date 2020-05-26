# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
from util.operationExcel import operationExcel
from base.SendRequests import sendrequests
from util.getRequestsdata import getresdata
from jsonpath_rw import jsonpath,parse
import json
class operationDpendData():
    def __init__(self,case_id):
        self.operExcel = operationExcel()
        self.sendres = sendrequests()
        self.getresdata = getresdata()
        self.case_id = case_id
    #获取依赖数据行
    def get_case_line_data(self):
        depend_data =  self.operExcel.get_rows_data(self.case_id)
        return depend_data
    #执行依赖的接口，获取依赖的数据
    def run_dependcase(self):
        row_num = self.operExcel.get_col_value().index(self.case_id)
        request_data = self.getresdata.get_res_data(row_num)
        url = self.getresdata.get_url(row_num)
        method = self.getresdata.get_method(row_num)
        headers = self.getresdata.is_headers(row_num)
        res = self.sendres.send_request(method,url,request_data,headers)
        return res
    #获取依赖数据key 对应的VALUE
    def get_dependdata_value(self,row):
        depend_data = self.getresdata.get_dep_jsonpath(row)
        response = self.run_dependcase()
        jsonpath_expr = parse(depend_data)
        return [match.value for match in jsonpath_expr.find(json.loads(response))][0]

if __name__ == '__main__':
    case_id = 'c001'
    res = operationDpendData(case_id)
    print(res.get_dependdata_value(4))




