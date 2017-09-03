# -*- coding: utf-8 -*-

import smtplib
import time
import codecs
import configparser
import email
from email.mime.text import MIMEText
from email.header import Header
#from email.mime.multipart import MIMEMultipart

CONFIG = "mail.conf"

c = configparser.ConfigParser()
c.readfp(codecs.open(CONFIG, "r", "utf-8-sig"))

mail_to = c.get("mail", "mail_to")
mail_to_list = mail_to.split(",")

mail_host = c.get("mail", "mail_host")
mail_alias = c.get("mail", "mail_alias")
mail_user = c.get("mail", "mail_user")
mail_pass = c.get("mail", "mail_pass")
mail_postfix = c.get("mail", "mail_postfix")

#print("[%s],%s,%s,%s,%s,%s" % (mail_to, mail_host, mail_alias, mail_user, mail_pass, mail_postfix))

def send(sub, content):

    me = u"%s<%s@%s>" % (mail_alias, mail_user, mail_postfix)
    mail_from = "<%s@%s>" % (mail_user, mail_postfix)

    header = Header(mail_alias, 'utf-8')
    header.append(mail_from, "ascii")

    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg["From"] = header

    """
    msg['To']字符串"a@b.com, c@d.com"
    sendmail参数mail_to为list
    """
    msg['To'] = mail_to

    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(me, mail_to_list, msg.as_string())
        server.close()
    except Exception as e:
        #print(e)
        return False
    return True


if __name__ == "__main__":

    sub = "短线高手提醒"
    content = "买601988中国银行\n买601988中国银行\n买601988中国银行\nthe end\n" + str(time.time())

    result = send(sub, content )
    print(result)



#end
