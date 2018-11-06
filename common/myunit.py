#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/10/23
import unittest,requests
from yc_object.page.apiclass import *
import logging,os
import logging.config

# path=os.path.dirname(os.path.dirname(__file__))
# logpath=os.path.join(path,"logs","log.config")
# CON_LOG='../logs/log.conf'
# # print(logpath1)
# #print(logpath)
# logging.config.fileConfig(CON_LOG)
# logging=logging.getLogger()
log_file_pa = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log.config')
log_file_path=log_file_pa.replace("\\","/")
logging.config.fileConfig(log_file_path)
logging=logging.getLogger()

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("test is start")
        self.s = requests.session()
        self.loc = apiclass(self.s,'18575686374','123456')
    def tearDown(self):
        logging.info("test is end")
        self.s.cookies.clear_session_cookies()
if __name__ == '__main__':
    unittest.main()