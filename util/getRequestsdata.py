from operationExcel import operationExcel
from operationGlobal import *
from operationJson import operationjson
class getresdata():
    def __init__(self):
        self.operExcel = operationExcel()
        self.glovar = global_var()
        self.get_lines = self.operExcel.get_nrows()
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
    #写入测试结果
    def write_result(self,row,vlaues):
        col = self.glovar.get_results_col()
        self.operExcel.write_cell_data(row,col,vlaues)

    #获取数据依赖ID
if __name__ == '__main__':
    print(getresdata().get_expect(0))

