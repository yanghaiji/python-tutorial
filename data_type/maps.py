#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: maps.py
@date: 2022/9/19 
"""

maps = {"id": 1, "name": "haiji", "adder": "beijing"}
print("maps 的值为 %s" % maps)

# 访问字典里的值
id = maps["id"]
print("id = %s" % id)

# pwd = maps["pwd"]
name = maps.get("name")
print("name = %s" % name)

pwd = maps.get("pwd", "1567")
print("pwd = %s" % pwd)

# 修改与添加
maps["adder"] = 'Beijing'
maps['pwd'] = '12345678'

print("adder = %s" % maps["adder"])
print("pwd = %s" % maps["pwd"])

print("maps.keys() = %s" % maps.keys())
print("maps.values() = %s" % maps.values())

del maps['name']  # 删除键是'Name'的条目
maps.clear()  # 清空字典所有条目
del maps  # 删除字典

print("maps 的值为 %s" % maps)
