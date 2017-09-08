# -*- coding: utf-8 -*-
import mail
import dxgs


MAIL_SUB = "短线高手提醒"


"""
1、09:31前，买入人数>30，为强势
2、截止09:35买入最多次数>=2的股票，基本在0-10之内
3、10:00，买入最多次数>=2的股票
   合计votes_count >= 80的股票
"""

"""
1、0936开始执行，获取所有股票，匹配0930时间，计算买入人数
2、1001开始执行，获取所有股票，买入最多次数，合计votes_count
"""


def main():
    print("main")


if __name__ == '__main__':
    main()
    content = "content"
    if mail.send(MAIL_SUB, content):





#end
