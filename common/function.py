#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/10/22
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import csv
#发送邮件方法
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class email():
# 进行带附件的邮件发送
    def send_mail(self,last_report):
        smtpserver = 'smtp.exmail.qq.com'
        username = 'xudegui@ubox.cn'
        password = '*******'
        sender = 'xudegui@ubox.cn'
        receiver = [ '308774117@qq.com']
        subject = '友唱接口测试报告'
        msg = MIMEMultipart('mixed')
        msg['Subject'] = subject
        msg['From'] = 'aaa'
            # 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
        msg['To'] = ";".join(receiver)
            # 构造文字内容
        text = "具体报告详情请见附件"
        text_plain = MIMEText(text, 'plain', 'utf-8')
        msg.attach(text_plain)
        sendfile = open(last_report , 'rb').read()
        text_att = MIMEText(sendfile, 'base64', 'utf-8')
        text_att["Content-Type"] = 'application/octet-stream'
        text_att.add_header('Content-Disposition', 'attachment', filename='个人测试报告.html')
        msg.attach(text_att)
        msgroot = MIMEMultipart()
        # msgroot.attach(MIMEText(content,'html','utf-8'))
        msgroot['Subject'] = subject
        msgroot['From'] = sender
        msgroot['To'] = ','.join(receiver)
         # 添加附件
        msgroot.attach(text_att)
        smtp = smtplib.SMTP_SSL(smtpserver, 465)
        smtp.helo(smtpserver)
        # 服务器返回结果确认
        smtp.ehlo(smtpserver)
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msgroot.as_string())
        smtp.quit()

    def latest_report(self,report_dir):
       list=os.listdir(report_dir)
       print (list)
       list.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
       file=os.path.join(report_dir,list[-1])
       return file

    def csv_file(self,csv_file,line):
        with open(csv_file,"r",encoding="utf-8-sig") as file:
            read=csv.reader(file)
            for index,row in enumerate(read,1):
                if index==line:
                    return row

if __name__ == '__main__':
    # csv_r='../data/yc.csv'
    # data=csv_file(csv_r,1)
    # print(data)
    report_dir = "../report"
    lare=email().latest_report(report_dir)
    print(lare)
    #email().send_mail(lare)

