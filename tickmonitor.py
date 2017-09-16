# -*- coding: utf-8 -*-

import tushare as ts
import numpy as np
from mail import mail
import time


today = time.strftime("%Y-%m-%d")

stock_code = '002312'
tick_volume = 1888
tick_type = '买盘'

#today = "2017-09-15"

sub = "*ST三泰[002312]1888买单"


df = ts.get_tick_data(stock_code, today)

print(time.strftime("%Y-%m-%d %H:%M:%S"))

if len(df) <= 3:
    """
                   time  price  change  volume  amount  type
    0  alert("当天没有数据");    NaN     NaN     NaN     NaN   NaN
    1   window.close();    NaN     NaN     NaN     NaN   NaN
    2         </script>    NaN     NaN     NaN     NaN   NaN
    """
    print("no data that day")
    exit(0)

selected = df[(df.volume == tick_volume) & (df.type == tick_type)]
if len(selected) == 0:
    print("no data selected")
    exit(0)


print("bingo")
mail.send(sub, str(selected))

if len(selected) >= 3:
    print(">= 3")
    time.sleep(5)
    mail.send(sub, str(selected))
    time.sleep(5)
    mail.send(sub, str(selected))

print("the end")

#end
