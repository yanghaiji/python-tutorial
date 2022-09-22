#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: for_loop.py
@date: 2022/9/20 
"""

seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for val in seq:
    print("当前元素为 %s" % val)

print("-" * 30)
for val in range(len(seq)):
    print("当前元素为 %s,其下标为 %s" % (seq[val], val))

for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:  # 确定第一个因子
            j = num / i  # 计算第二个因子
            print('%d 等于 %d * %d' % (num, i, j))
            break  # 跳出当前循环
    else:  # 循环的 else 部分
        print('%d 是一个质数' % num)

print("-" * 30)
dicts = {
    "id": 1,
    "name": "haiji",
    "pwd": "123456789"
}
# 同时获取 key value
for k, v in dicts.items():
    print("dicts key = %s , value = %s" % (k, v))
print("-" * 30)
# 获取所有的 key
for key in dicts.keys():
    print("dicts key = %s" % key)
print("-" * 30)
# 获取所有的 value
for value in dicts.values():
    print("dicts value = %s" % value)
