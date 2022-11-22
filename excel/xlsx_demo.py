#!/usr/bin/env python
# coding=utf-8

"""
<p>
读取excel
</p>
@author: hai ji
@file: xlsx_demo.py
@date: 2022/11/21 
"""
import os
import pathlib

import xlrd


def get_excel_data(filename, sheet_name):
    """
    读取excel文件
    :param filename:  文件名
    :param sheet_name: sheet 名字
    :return:
    """
    # 调用函数，获取当前项目根目录
    project_path = str(pathlib.Path(os.getcwd())) + '/'
    # project_path = os.getcwd() + '/'
    file_path = project_path + filename  # 读取的excel文件路径
    lst_data = []
    work_book = xlrd.open_workbook(file_path)
    work_sheet = work_book.sheet_by_name(sheet_name)
    rows = work_sheet.nrows
    cols = work_sheet.ncols
    for row in range(1, rows):  # 遍历时不取第一行表头内容
        row_list = []
        for col in range(cols):
            cell_data = work_sheet.cell_value(row, col)
            row_list.append(cell_data)  # 每一行的内容都放到一个列表中
        lst_data.append(row_list)  # 把多行内容放到同一个列表中
    return lst_data


if __name__ == '__main__':
    excelList = get_excel_data('red_excel.xlsx', 'Sheet1')
    # print(excelList)
    for a in excelList:
        print(a)
        # for val in a:
        #     print(val)
    # print(str(pathlib.Path(os.getcwd())))
