# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
from util.operationExcel import operationExcel
from base.SendRequests import sendrequests
from util.getRequestsdata import getresdata
class operationDpendData():
    def __init__(self):
        self.operExcel = operationExcel()
        self.sendres = sendrequests()
        self.getresdata = getresdata()
    #获取依赖数据行
    def get_case_line_data(self,case_id):
        depend_data =  self.operExcel.get_rows_data(case_id)
        return depend_data
    #执行依赖的接口，获取依赖的数据
    def run_dependcase(self,case_id):
        row_num = self.operExcel.get_col_value().index(case_id)
        request_data = self.getresdata.get_res_data(row_num)
        url = self.getresdata.get_url(row_num)
        method = self.getresdata.get_method(row_num)
        headers = self.getresdata.is_headers(row_num)
        res = self.sendres.send_request(method,url,request_data,headers)
        return res
if __name__ == '__main__':
    res = operationDpendData()
    case_id = 'c001'
    res.run_dependcase(case_id)



