# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
import time
from base.SendRequests import sendrequests
from util.getRequestsdata import getresdata
from util.operationExcel import operationExcel
from util.judgeStr import judgestr
from common.DpendData import operationDpendData
class testrunner():
    def __init__(self):
        day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
        self.getData = getresdata()
        self.sendrequest = sendrequests()
        self.operationExcel = operationExcel()
        self.filenamepath = r'D:\PyCharmProject\api-test-python3\report\%s-report.html'%day
    def run_main(self):
        print(self.filenamepath)
        nrows = self.operationExcel.get_nrows()
        for i in range(1,nrows):
            url = self.getData.get_url(i)
            params = self.getData.get_res_data(i)
            method = self.getData.get_method(i)
            headers = self.getData.is_headers(i)
            expect = self.getData.get_expect(i)
            dep_caseid = self.getData.get_dep_caseid(i)
            if self.getData.is_run(i):
                if dep_caseid != '':
                    dep_values = operationDpendData(dep_caseid).get_dependdata_value(i)
                    dep_file = self.getData.get_dep_file(i)
                    params[dep_file] = dep_values
                res = self.sendrequest.send_request(method, url, params, headers)
                if judgestr(res,expect).includestr():
                    self.getData.write_result(i,res)
                    self.getData.write_is_pass(i,'Pass')
                    print('测试通过')
                else:
                    self.getData.write_result(i,res)
                    self.getData.write_is_pass(i, 'Fail')
                    print('测试失败')
if __name__ == '__main__':
    testrunner().run_main()