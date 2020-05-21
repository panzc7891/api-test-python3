# -*- coding: utf-8 -*-
"""
Created on 2020-05-08
@author: panzhaochao
"""
class judgestr():
    def __init__(self,str1,str2):
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

if __name__ == '__main__':
    str1 = 'name'
    str2 = 'a'
    res = judgestr(str1,str2)
    print(res.includestr())
    print(res.equalstr())


