#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: functions.py
@date: 2022/9/20 
"""


def func_sum(a: int, b: int):
    print("这是第一个函数测试")
    return a + b


sums = func_sum(10, 22)
print(sums)


def printinfo(mark, msg):
    print("mark :%s" % mark)
    print("msg :%s" % msg)


printinfo(msg="这是一条消息", mark="INFO")

print("-" * 30)


def printinfo2(msg, mark="INFO"):
    print("mark :%s" % mark)
    print("msg :%s" % msg)


printinfo2(msg="这是一条自带默认 mark的消息")
print("-" * 30)


def printinfo3(mark, msg, *var):
    print("mark :%s" % mark)
    print("msg :%s" % msg)
    for value in var:
        print(value)


printinfo3("INFO", "这是一条消息", "不定长参数1", "不定长参数2", "不定长参数3")
print("-" * 30)


def printinfo4(mark, msg, **var):
    print("mark :%s" % mark)
    print("msg :%s" % msg)
    for key, value in var.items():
        print("不定长参数 key= %s value =  %s" % (key, value))


printinfo4(msg="这是一条消息", mark="INFO", age=28, pwd="12345678")
print("-" * 30)

sub = lambda a, b: a - b

print("lambda 内部函数计算的值 : %s" % sub(100, 30))
