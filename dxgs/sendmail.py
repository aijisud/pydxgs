# -*- coding: utf-8 -*-

import smtplib
import time
from email.mime.text import MIMEText

def send_mail(sub,content):

    #mail_to="dsj3578@mail.notes.bank-of-china.com"
    mail_to="aijisud@163.com"

    mail_host="smtp.sina.com"  #设置服务器
    mail_user="aijisud"    #用户名
    mail_pass="PI314ei27we"   #口令
    mail_postfix="sina.com"  #发件箱的后缀

    me="Monitor"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain',_charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = mail_to
    server = smtplib.SMTP()
    server.connect(mail_host)
    server.login(mail_user,mail_pass)
    server.sendmail(me, mail_to, msg.as_string())
    server.close()
    return True
