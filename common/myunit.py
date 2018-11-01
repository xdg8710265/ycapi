#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/10/23
import unittest,requests
from yc_object.page.apiclass import *
import logging,os
import logging.config

path=os.path.dirname(os.path.dirname(__file__))
logpath=os.path.join(path,"log","log.config")
# CON_LOG='./log/log.conf'
print(logpath)
logging.config.fileConfig(logpath)
logging=logging.getLogger()

class StartEnd(unittest.TestCase):
    def setUp(self):
        logging.info("test is start")
        self.s = requests.session()
        lo = apiclass(self.s)
        lo.login("18575686374", '123456')
        self.loc = apiclass(self.s)

    def tearDown(self):
        logging.info("test is end")
        self.s.cookies.clear_session_cookies()
# if __name__ == '__main__':
#     unittest.main()