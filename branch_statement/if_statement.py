#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: if_statement.py
@date: 2022/9/20 
"""

m = 10000000

if m > 1000000:
    print("你的资金量非常充足，你可以做些你喜欢的事情！")
else:
    print("你的资金量不是很充足，加油吧打工人！！！")

age = 28
if 7 < age < 18:
    print("你还未成年")
elif 18 < age < 35:
    print("你已经成年")
elif 35 < age < 55:
    print("你已步入中年")
elif age > 55:
    print("你已步入老年")
else:
    print("你的年龄还太小")
