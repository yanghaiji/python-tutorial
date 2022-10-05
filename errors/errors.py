#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: errors.py
@date: 2022/9/22 
"""


# while True print('Hello world')

# def conversion(total):
#     num = int(total)
#     return "@" * num
#
#
# print(conversion(2))
# print(conversion("t"))


def conversion(total):
    try:
        num = int(total)
        print("@" * num)
    except ValueError as e:
        print("程序处理发生异常，请检查您的参数！")


# conversion(2)
# conversion("t")


def err_else(total):
    try:
        num = int(total)
        print("@" * num)
    except ValueError as e:
        print("程序处理发生异常，请检查您的参数！")
    else:
        print("@")


# err_else(2)
# err_else("t")


def err_else_e(total):
    num = 100 / total
    print("-" * num)


def err_else_conversion(total):
    try:
        print(total)
    except ValueError as e:
        print("程序处理发生异常，请检查您的参数！")
    else:
        err_else_e(total)


# err_else_conversion(0)


def error_raise():
    try:
        10 / 0
    except ZeroDivisionError as e:
        raise


# error_raise()


def error_finally():
    try:
        10 / 0
    except ZeroDivisionError as e:
        raise
    finally:
        print("此代码无论是否发生异常都会被执行")


error_finally()
