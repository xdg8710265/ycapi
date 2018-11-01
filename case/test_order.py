#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/10/23
from yc_object.common.myunit import *
import logging
from yc_object.common.function import csv_file


class TestOrder(StartEnd):
    def test_01(self):
        '''接口参数正常'''
        logging.info("the adfun is normal")
        result=self.loc.adorder("3321","1023ad111")
        self.assertEqual(result['response']['result_code'],'false')
    def test_02(self):
        '''请求的参数号错误'''
        logging.info("the adfun is error")
        result = self.loc.adorder("332","adtest1")
        self.assertEqual(result['response']['result_code'], 'false')
        #self.assertEqual(result['response']['error_msg'], '接口号有误！')
    def test_03(self):
        '''请求的参数号正确，名字已经存在'''
        logging.info("the adname is exit")
        result=self.loc.adorder("3321","1023ad")
        #print(result)
        self.assertEqual(result['response']['result_code'], 'false')
if __name__ == '__main__':
    unittest.main()