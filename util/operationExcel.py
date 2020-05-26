# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
import xlrd
from xlutils.copy import copy
class operationExcel:
    def __init__(self,filename=None,sheetid=None):
        if filename:
            self.filename = filename
            self.sheetid = sheetid
        else:
            self.filename = r'D:\PyCharmProject\api-test-python3\data\test.xls'
            self.sheetid = 0
        self.table = self.get_tables()
    #获取表格内容
    def get_tables(self):
        data = xlrd.open_workbook(self.filename)
        sheet = data.sheet_by_index(self.sheetid)
        return sheet
    #获取单元格
    def get_cell_value(self,row,col):
        table = self.table
        cell_value = table.cell_value(row,col)
        return cell_value
    #获取行数
    def get_nrows(self):
        table = self.table
        nrows = table.nrows
        return nrows
    #获取某一列值
    def get_col_value(self,col= None):
        colvalue = []
        if col != None:
            for i in range(0,self.get_nrows()):
                cols = self.get_cell_value(i,col)
                colvalue.append(cols)
        else:
            colvalue = self.get_col_value(0)
        return colvalue
    def write_cell_data(self,row,col,value):
        '''
        写数据
        '''
        workbook = xlrd.open_workbook(self.filename)
        new_workbook = copy(workbook)
        new_sheets = new_workbook.get_sheet(0)
        new_sheets.write(row,col,value)
        new_workbook.save(self.filename)
        return None

    # 根据对应的caseID找到对应行内容
    def get_rows_data(self,case_id):
        table = self.table #获取表格内容
        #caseid_data = self.get_col_value()   #获取依赖CASEID的值
        row_num = self.get_col_value().index(case_id)  #获取依赖CASEID行对应的行值
        row_data = table.row_values(row_num)   # 获取依赖CASEID行对应的内容
        return row_data
    # def get_rows_data(self,case_id):
    #     row_num = self.get_rows_num(case_id)
    #     row_data = self.get_row_values(row_num)
    #     return row_data
    # #根据对应的case_id找到对应行的行号
    # def get_rows_num(self,case_id):
    #     caseiddata = self.get_col_value()
    #     rows_num = caseiddata.index(case_id)
    #     return rows_num
    # #根据对应的行号找到对应行的内容
    # def get_row_values(self,rownum):
    #     table = self.table
    #     row_data = table.row_values(rownum)
    #     return row_data

if __name__ == '__main__':
    res = operationExcel()
    table = res.get_tables()
    cell = res.get_cell_value(0,0)
    rows = res.get_nrows()
    cols = res.get_col_value()

    case_id = 'c003'
    data = res.get_rows_data(case_id)
    print(data)
    # print(table)
    # print(cell)
    # print(rows)
    #print(cols)
