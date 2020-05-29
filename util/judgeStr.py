# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
class judgestr():
    def __init__(self,str1=None,str2=None):
        self.str1 = str1
        self.str2 = str2
    def includestr(self):
        """
        #判断字符串包含
        """
        if self.str1.find(self.str2) == -1:
            return False
        else:
            return True

    def equalstr(self):
        """
        #判断字符串相等
        """
        if self.str1 == self.str2:
            return True
        else:
            return False
    def judge_number(self,_list,key):
        """
        #判断列表中元素的某个元素的个数
        """
        dict = {}
        for i in _list:
            dict[i] = dict.get(i,0)+1
        return dict[key]


