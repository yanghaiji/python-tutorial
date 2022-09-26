#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: lists.py
@date: 2022/9/19 
"""

# 创建一个列表
list1 = [0, 1, 2, 3, 4, 5, 6, 7, "python", True, 20.1]

# 根据下标查询
print("list1[1]= %s" % list1[1])
# 数据 1-3
print("list1[1:3]= %s" % list1[1:3])

list1.append("append")

# 修改数据
list1[11] = "app"

# 删除数据
list1.remove(20.1)

list1.insert(len(list1), "insert")

list1.reverse()
a = 0
for i in list1:
    print("list1[ %s ]= %s" % (a, i))
    a += 1
list2 = [0, 29, 2, 3, 4, 2, 6, 7]
list2.sort()
for i in list2:
    print("list2[ %s ]= %s" % (a, i))
    a += 1
