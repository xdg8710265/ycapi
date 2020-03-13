#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/10/23
import unittest,os
#from HTMLTestRunner import HTMLTestRunner
from BSTestRunner import BSTestRunner
import time
from yc_object.common.function import *
import logging
test_dir1=os.path.dirname(__file__)
#print(test_dir1)
test_dir=os.path.join(test_dir1,'case').replace("\\","/")

report_dir="./report"

descover=unittest.defaultTestLoader.discover(test_dir,pattern="test_cuba.py")

now=time.strftime("%Y-%m-%d %H-%M-%S")

report_name=report_dir+'/'+now+"report.html"

with open(report_name,'wb') as f:
    runner=BSTestRunner(stream=f,title="友唱接测试",description="接口测试报告")
    run=runner.run(descover)

#("获取最后一个报告")
logging.info("————获取最后一个测试报告————")
lastr=email.latest_report(report_dir)

#("发送邮件")
logging.info("---发送邮件---")
email.send_mail(lastr)
