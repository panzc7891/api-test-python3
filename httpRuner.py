# -*- coding: utf-8 -*-
"""
Created on 2020-01-08
@author: panzhaochao
"""
import time
from common.GetConfData import getConfingdata
from base.TestRunner import testrunner
from common.CreateReport import CreateReport
class httpRunner():
    def __init__(self):
        filepath1 = getConfingdata().get_conf_data(_key='filenamepath',_value='report')
        day = time.strftime("%Y%m%d%H%M", time.localtime())
        self._Report = CreateReport()
        self._Run = testrunner()
        self.filepath = filepath1 + '%(report)s-report.html' % dict(report=day)
        self.title = '接口测试报告'
    def run(self):
        starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self._Run.run_main()
        endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self._Report.create_report_html(self.filepath,self.title,starttime,endtime)
        print('执行成功')
if __name__ == '__main__':
    httpRunner().run()
