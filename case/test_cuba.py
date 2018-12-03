#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/12/3
from yc_object.common.myunit import *
import logging
from yc_object.common.function import csv_file
import unittest
class TestCuba(StartEnd):
    def test_01(self):
        logging.info("未联网分析商家接口是正确的")
        result = self.loc.shopdetail()
        self.assertEqual(result['response']['result_code'], 'true')
    @unittest.skip("跳过测试")
    def test_02(self):
        logging.info("未联网分析商家接口请求参数错误")
        result = self.loc.shopdetail()
        self.assertEqual(result['response']['result_code'], 'false')