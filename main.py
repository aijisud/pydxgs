# -*- coding: utf-8 -*-
import mail
import dxgs


MAIL_SUB = "短线高手提醒"


def main():
    print("main")


if __name__ == '__main__':
    main()
    content = "content"
    if mail.send(MAIL_SUB, content):
        print("mail send")


#end
