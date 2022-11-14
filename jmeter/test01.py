#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: test01.py
@date: 2022/11/4 
"""
import datetime
import os
import subprocess

jmx_file = 'jmx/test01.jmx'  # jmx文件路径
result_file = 'jmx/test01.jtl'  #
log_file = 'run.log'
date = datetime.datetime.now()
# report存放的路径
report_dir = 'report/' + date.strftime("%Y%m%d") + '/' + date.strftime("%H%M%S")
# 不存在则创建
if not os.path.exists(report_dir):
    os.makedirs(report_dir)

run_cmd = f'jmeter -n -t {jmx_file} -l {result_file} -j {log_file}'  # 无界面运行JMeter压测命令
report_cmd = f'jmeter -g {result_file} -o {report_dir}'  # 生成HTML报告命令

# 不需要获取屏幕输出是，可以使用os.system()
# os.system(run_cmd)
# os.system(report_cmd)

# 需要获取屏幕输出是，可以使用subprocess.Popen()
p1 = subprocess.Popen(run_cmd, shell=True, stdout=subprocess.PIPE)
print(p1.stdout.read().decode('utf-8'))
p2 = subprocess.Popen(report_cmd, shell=True, stdout=subprocess.PIPE)
print(p2.stdout.read().decode('utf-8'))
