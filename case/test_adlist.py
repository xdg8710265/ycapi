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
        self.assertEqual(result['response']['result_code'],'true')
        #print(result)
    def test_adlist_funr_typew(self):
        """广告列表序列号错误，类型正确"""
        list_file = "../data/adlist.csv"
        logging.info("adlist fun is right type error")
        data = csv_file(list_file, 2)
        result = self.loc.adlist(data[0], data[1])
        self.assertEqual(result['response']['result_code'], 'false')

    def test_adlist_funw_typer(self):
        """广告列表序列号正确，类型错误"""
        list_file = "../data/adlist.csv"
        logging.info("adlist fun is wrong type right")
        data = csv_file(list_file, 3)
        result = self.loc.adlist(data[0], data[1])
        self.assertEqual(result['response']['result_code'], 'false')
    def test_adlist_funw_typew(self):
        """广告列表序列号正确，类型正确"""
        list_file = "../data/adlist.csv"
        logging.info("adlist fun is wrong type wrong")
        data = csv_file(list_file, 4)
        result = self.loc.adlist(data[0], data[1])
        self.assertEqual(result['response']['result_code'], 'true')
        #print(result)

if __name__ == '__main__':
    unittest.main()
