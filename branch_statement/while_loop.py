#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: while_loop.py
@date: 2022/9/20 
"""

# 循环10次后程序终止
i = 1
while i <= 10:
    print("这是第 %s 次循环" % i)
    i += 1
print("-" * 30)
i = 1
while i <= 10:
    if i == 8:
        break
    print("这是第 %s 次循环" % i)
    i += 1

print("-" * 30)
i = 1
while i <= 10:
    if i == 8:
        print("第 %s 次循环 以跳过" % i)
        # i += 1
        continue
    print("这是第 %s 次循环" % i)
    i += 1
