#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/11/1
from yc_object.common.myunit import *
from yc_object.common.function import csv_file
import logging

class TestAdlist(StartEnd):
    def test_adlistnormal(self):
        """广告列表正常显示"""
        list_file="../data/adlist.csv"
        logging.info("adlist is normal")
        data=csv_file(list_file,1)
        result=self.loc.adlist(data[0],data[1])
        self.assertTrue(result['response']['result_code'],'true')
if __name__ == '__main__':
    unittest.main()
