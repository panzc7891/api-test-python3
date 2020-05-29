# -*- coding: utf-8 -*-
"""
Created on 2020-01-08
@author: panzhaochao
"""
import xlrd
from common.GetConfData import getConfingdata
from xlutils.copy import copy
class operationExcel:
    def __init__(self):
        self.filename = getConfingdata().get_conf_data(_key='filenamepath',_value='excelfile')
        #self.filename = 'D:\PyCharmProject\\auto-api-test\data\\test.xls'
        self.sheetid = 0
        self.table = self.get_tables()
    #获取表格内容
    def get_tables(self):
        data = xlrd.open_workbook(self.filename)
        sheet = data.sheet_by_index(self.sheetid)
        #print(sheet)
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
if __name__ =='__main__':
    operationExcel().get_tables()
