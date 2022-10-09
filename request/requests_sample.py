#!/usr/bin/env python
# coding=utf-8

"""
<p>
request 相关示例代码
</p>
@author: hai ji
@file: requests_sample.py
@date: 2022/9/28 
"""
import requests


def sm():
    # 发送请求
    x = requests.get('https://www.baidu.com/')

    # 返回网页内容
    print(x.text)
    # 返回 http 的状态码
    print(x.status_code)

    # 响应状态的描述
    print(x.reason)

    # 返回编码
    print(x.apparent_encoding)


def sm_headers():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    sm_headers = requests.get('https://www.baidu.com/', headers=headers)
    print(sm_headers.status_code)


def sm_post():
    datas = {
        "id": 1,
        "name": "haiji",
        "weChat": "372787553"
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
    }
    sm_headers = requests.post('http://localhost:8080/json/', headers=headers, data=datas)
    print(sm_headers.status_code)


sm_headers()
