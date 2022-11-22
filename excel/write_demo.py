#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: write_demo.py
@date: 2022/11/22 
"""
import xlwt


def write_excel(path, filename):
    # 创建 xls 文件对象
    wb = xlwt.Workbook(encoding='utf-8')

    # 新增两个表单页
    sh1 = wb.add_sheet('成员名单')
    sh2 = wb.add_sheet('附加信息')

    # 然后按照位置来添加数据,第一个参数是行，第二个参数是列

    for a in range(10):
        # 写入第一个sheet
        if a == 0:
            sh1.write(0, 0, '姓名')
            sh1.write(0, 1, '联系电话')
        else:
            sh1.write(a, 0, '张三' + str(a))
            sh1.write(a, 1, a)

    # 写入第二个sheet
    sh2.write(0, 0, '总人数')
    sh2.write(1, 0, 9)

    # 最后保存文件即可
    wb.save(filename)


if __name__ == '__main__':
    write_excel(None, 'test.xls')

    # for a in range(10):
    #     print(a)
