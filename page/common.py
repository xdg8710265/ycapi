#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2020/3/13
import requests
class Common():
    def __init__(self,urlroot):
        #统一路径的url
        self.url=urlroot
    def get(self,url,params=""):
        url=self.url
        res=requests.get(url)
        return res
    def post(self,uri,params=""):
        url=self.url+uri
        if len(params)>0:
            res=requests.post(url,data=params)
        else:
            res=requests.post(url)
        return res