#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/10/22

import requests


import json
class apiclass():
     #初始话
    def __init__(self,s):
        self.s=s  #传递一个行参
    def login(self,phone, passwd):
        url="http://pre-admin-pc.ucmbar.com/youCS/youC/admin/index/api"
        data = {
            "header": {"data_type": "normal", "data_direction": "request", "server": "YoucManage", "id": "YoucManage"},
            "request": {"function": "1001", "version": "1.0", "mobile": phone, "password": passwd},
            "comment": []}
        reslut =self.s.post(url=url, json=data)
        return reslut.json()
    def adposition(self,fun):
        url="http://pre-admin-pc.ucmbar.com/youCS/youC/admin/Synthesize/api"
        data={
            "header":{"data_type":"normal","data_direction":"request","server":"YoucManage","id":"YoucManage"},
            "request":{"function":fun,"version":"1.0"},
            "comment":""}
        result=self.s.post(url=url,json=data)
        return result.json()
    def adorder(self,fun,adname):

        url = "http://pre-admin-pc.ucmbar.com/youCS/youC/admin/Synthesize/api"
        data={
            "header":{"data_type":"normal","data_direction":"request","server":"YoucManage","id":"YoucManage"},
	        "request":{"function":fun,"version":"1.0","name":adname,"start_time":"2018-10-26","end_time":"2018-10-27",
		                "type":"1000","click_type":"2","click_content":"更改11","picture_url":"http://ahead-test.oss-cn-hangzhou.aliyuncs.com/youCTest/153611865311515.png",
                        "list_order":"1","desc":"备注描述11","set_condition":"1","property":[],"provinces":[],"city":[],
                        "account_type":[1,2],"sort":"timestamp"},
	        "comment":""}

        result=self.s.post(url=url,json=data)
        return result.json()

if __name__ == '__main__':
    s = requests.session()
    b=apiclass(s)
    a=b.login('18575686374','123456')
    print(a)
    c=b.adorder("3321","1023ad")
    print(c)

