#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: mysql_inset.py
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

# SQL 插入语句
# sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
#          # LAST_NAME, AGE, SEX, INCOME)
#          # VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(FIRST_NAME, \
       LAST_NAME, AGE, SEX, INCOME) \
       VALUES ('%s', '%s',  %s,  '%s',  %s)" % \
       ('Mac', 'Mohan', 20, 'M', 2000)
try:
    # 执行sql语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 关闭数据库连接
db.close()
