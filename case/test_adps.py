#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/10/22
from yc_object.common.myunit import *
from yc_object.common.function import *
import logging
import logging.config

class TestAdps(StartEnd):
    def test_01(self):
        '''接口请求参数正常'''
        csv_r = './data/yc.csv'
        data =csv_file(csv_r,2)
        logging.info("the adfun is normal")
        result=self.loc.adposition(data[0])
        self.assertEqual(result['response']['result_code'],'true')
    def test_02(self):
        '''接口请求参数为大于1时'''
        logging.info("the adfun is error")
        result = self.loc.adposition(3321)
        self.assertEqual(result['response']['result_code'], 'false')
    def test_03(self):
        '''接口请求参数为小于1时'''
        logging.info("the adfun is error")
        result = self.loc.adposition(3319)
        self.assertEqual(result['response']['result_code'], 'false')

if __name__ == '__main__':
    unittest.main()