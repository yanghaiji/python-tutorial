#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: common_functions.py
@date: 2022/9/21 
"""
import time
import calendar

"""
range 函数说明
"""
# 0 到 9 范围内的数据，左闭右开原则
ran = range(10)
print(type(ran))
for r in ran:
    print(r)

print("-" * 30)
# 0 到 9 范围内的数据,且步长为2

ran = range(0, 10, 2)

for r in ran:
    print(r)

print("-" * 30)

# 生成 list

list_num = list(range(5, 10))

for i in list_num:
    print(i)
print("-" * 30)

"""
类型判断函数
"""

ran = range(10)
num = 10

print("ran 的类型是 %s" % type(ran))
print("num 的类型是 %s" % type(num))

"""
时间类型函数
"""

ticks = time.time()
print("当前时间戳为:", ticks)

localtime = time.localtime(time.time())
print("本地时间为 :", localtime)

localtime = time.asctime(time.localtime(time.time()))
print("本地时间为 :", localtime)

# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 格式化成Sat Mar 28 22:24:24 2016形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))


cal = calendar.month(2022, 9)
print("以下输出2022年9月份的日历:", cal)
