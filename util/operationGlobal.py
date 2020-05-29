# -*- coding: utf-8 -*-
"""
Created on 2020-01-08
@author: panzhaochao
"""
class global_var():
    id = '0'  #caseid
    casename = '1' #casename
    url = '2' #请求URL
    request_method = '3' #请求方法
    is_run = '4' # 是否执行
    header = '5'  #是否携带header
    case_depend_id = '6' # 数据依赖id
    data_depend_jsonpath = '7'  #依赖的数据
    file_depend = '8'  #依赖字段
    request_data = '9' #请求数据
    excpect = '10' #期望结果
    results = '11' #实际结果
    is_pass = '12' #是否通过
    def get_id_col(self):
        return int(global_var.id)

    def get_casename_col(self):
        return int(global_var.casename)

    def get_url_col(self):
        return int(global_var.url)

    def get_request_method_col(self):
        return int(global_var.request_method)

    def get_is_run_col(self):
        return int(global_var.is_run)

    def get_header_col(self):
        return int(global_var.header)
    #获取header的值
    def get_header_values(self):
        headers = {'Content-Type':'application/json'}
        return headers

    def get_case_dependid_col(self):
        return int(global_var.case_depend_id)

    def get_data_dependjsonpath_col(self):
        return int(global_var.data_depend_jsonpath)

    def get_file_depend_col(self):
        return int(global_var.file_depend)

    def get_request_data_col(self):
        return int(global_var.request_data)

    def get_excpect_col(self):
        return int(global_var.excpect)

    def get_results_col(self):
        return int(global_var.results)

    def get_is_pass_col(self):
        return int(global_var.is_pass)

    def case_depend_col(self):
        return int(global_var.results)


if __name__ == '__main__':
    res = global_var()
    e = res.get_url_col()
    print(e)