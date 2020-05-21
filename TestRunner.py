# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
from base.SendRequests import sendrequests
from util.getRequestsdata import getresdata
from util.operationExcel import operationExcel
from util.judgeStr import judgestr
class testrunner():
    def __init__(self):
        self.getData = getresdata()
        self.sendrequest = sendrequests()
        self.operationExcel = operationExcel()
    def run_main(self):
        nrows = self.operationExcel.get_nrows()
        for i in range(1,nrows):
            url = self.getData.get_url(i)
            params = self.getData.get_res_data(i)
            method = self.getData.get_method(i)
            headers = self.getData.is_headers(i)
            expect = self.getData.get_expect(i)
            if self.getData.is_run(i):
                res = self.sendrequest.send_request(method,url,params,headers)
                #print(res)
                if judgestr(res,expect).includestr():
                    self.getData.write_result(i,'测试通过')
                    #print('测试通过')
                else:
                    self.getData.write_result(i,'测试失败')
                    #print('测试失败')
if __name__ == '__main__':
    testrunner().run_main()