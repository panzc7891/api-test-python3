# -*- coding: utf-8 -*-
"""
Created on 2020-01-08
@author: panzhaochao
"""
import configparser
class getConfingdata():
    def __init__(self):
        self.confingpath = r'D:\PyCharmProject\auto-api-test\config\config.ini'

    def get_conf_data(self,_key,_value):
        '''
        获取配置文件的数据
        '''
        try:
            conf = configparser.ConfigParser()
            conf.read(self.confingpath, 'utf-8')
            values = conf.get(_key, _value)
            return values
        except Exception as e:
            return ('读取配置文件失败，请检查获取的关键字内容是否存在：%s'%e)
if __name__ == '__main__':
    filenamepath = 'filenamepath'
    excelfilename = 'excelfilename'
    s = getConfingdata().get_conf_data(filenamepath,excelfilename)
    print(s)