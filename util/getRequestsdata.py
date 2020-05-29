# -*- coding: utf-8 -*-
"""
Created on 2020-01-08
@author: panzhaochao
"""
from operationExcel import operationExcel
from operationGlobal import *
from operationJson import operationjson
class getresdata():
    def __init__(self):
        self.operExcel = operationExcel()
        self.glovar = global_var()
        self.get_lines = self.operExcel.get_nrows()
    #获取用例ID
    def get_case_id(self,row):
        col = self.glovar.get_id_col()
        return self.operExcel.get_cell_value(row,col)
    #获取用例名称
    def get_case_name(self,row):
        col = self.glovar.get_casename_col()
        return self.operExcel.get_cell_value(row,col)
    #是否执行
    def is_run(self,row):
        col = self.glovar.get_is_run_col()
        if self.operExcel.get_cell_value(row,col) == 'yes':
            return True
        else:
            return False
    #是否携带header
    def is_headers(self,row):
        col =  self.glovar.get_header_col()
        if self.operExcel.get_cell_value(row,col) == 'yes':
            return global_var().get_header_values()
        else:
            return None
    #获取URL
    def get_url(self,row):
        col = self.glovar.get_url_col()
        return self.operExcel.get_cell_value(row,col)
    #获取请求方法
    def get_method(self,row):
        col = self.glovar.get_request_method_col()
        return self.operExcel.get_cell_value(row,col)
    #获取请求数据
    def get_res_data(self,row):
        col = self.glovar.get_request_data_col()
        data = self.operExcel.get_cell_value(row,col)
        json_data = operationjson().get_josn_key_data(data)
        if data == '':
            return None
        else:
            return json_data
    #获取期望结果
    def get_expect(self,row):
        col = self.glovar.get_excpect_col()
        expect = self.operExcel.get_cell_value(row,col)
        if expect == '':
            return None
        else:
            return expect
    #获取依赖数据的caseID
    def get_dep_caseid(self,row):
        col = self.glovar.get_case_dependid_col()
        dep_caseid = self.operExcel.get_cell_value(row,col)
        return dep_caseid
    #获取依赖的数据取值的(jsonpath)
    def get_dep_jsonpath(self,row):
        col = self.glovar.get_data_dependjsonpath_col()
        dep_jsonpath = self.operExcel.get_cell_value(row,col)
        return dep_jsonpath
    #获取依赖字段
    def get_dep_file(self,row):
        col = self.glovar.get_file_depend_col()
        dep_file = self.operExcel.get_cell_value(row,col)
        return dep_file
    #写入实际返回结果
    def write_result(self,row,vlaues):
        col = self.glovar.get_results_col()
        self.operExcel.write_cell_data(row,col,vlaues)
    #写入是否通过
    def write_is_pass(self,row,values):
        col = self.glovar.get_is_pass_col()
        self.operExcel.write_cell_data(row,col,values)
    #获取实际结果
    def get_results(self,row):
        col = self.glovar.get_results_col()
        return self.operExcel.get_cell_value(row,col)
    #获取是否通过
    def get_is_pass(self,row):
        col = self.glovar.get_is_pass_col()
        return self.operExcel.get_cell_value(row,col)
