#!/usr/bin/env python
# coding=utf-8

"""
<p>
mysql 连接示例
</p>
@author: hai ji
@file: mysql_connect.py
@date: 2022/11/1 
"""

import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     port=3307,
                     user='root',
                     password='123456',
                     database='TESTDB')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()
