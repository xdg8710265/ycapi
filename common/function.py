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
def send_mail(latest_report):
    f=open(latest_report,'rb')
    mail_content=f.read()
    f.close()
    smtpserver="smtp.163.com"
    username="15070315464@163.com"
    password="xdg1990920"
    send="15070315464@163.com"
    recive=['xudegui@ubox.cn']
    subject=u"这是个测试封装好的发送"
    msg=MIMEText(mail_content,'html','utf-8')
    msg['Subject']=Header(subject)
    msg['From']=send
    msg['To']=','.join(recive)

    smtp=smtplib.SMTP_SSL(smtpserver,465)
    smtp.helo(smtpserver)
    smtp.ehlo(smtpserver)
    smtp.login(username,password)
    smtp.sendmail(send,recive,msg.as_string())
    smtp.quit()
    print ("end")

def latest_report(report_dir):
   list=os.listdir(report_dir)
   print (list)
   list.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
   file=os.path.join(report_dir,list[-1])
   return file

def csv_file(csv_file,line):
    with open(csv_file,"r",encoding="utf-8-sig") as file:
        read=csv.reader(file)
        for index,row in enumerate(read,1):
            if index==line:
                return row


if __name__ == '__main__':
    csv_r='../data/yc.csv'
    data=csv_file(csv_r,1)
    print(data)

    report="../report"
    lare=latest_report(report)
    send_mail(lare)