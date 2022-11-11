#!/usr/bin/env python
# coding=utf-8

"""
<p>
接口自动化测试
</p>
@author: hai ji
@file: itf_demo.py
@date: 2022/11/11 
"""
import pytest
import requests


# def test_baidu_home():
#     """
#     测试访问百度首页
#     这里需要用到request 包
#     :return:
#     """
#     # 发送请求
#     x = requests.get('https://www.baidu.com/')
#
#     # 返回网页内容
#     print(x.text)
#     # 返回 http 的状态码
#     assert x.status_code == 200


# https://www.baidu.com/s?ie=utf-8&wd=ptytest
#
# def test_baidu_search():
#     """
#     测试访问百度首页搜素pytest项目的内容
#     这里需要用到request 包
#     :return:
#     """
#     # 发送请求
#     x = requests.get('https://www.baidu.com/s?ie=utf-8&wd=ptytest')
#
#     # 返回 http 的状态码
#     assert x.status_code == 200
#     # 返回网页内容 是否包含 pytest
#     assert str(x.text).find('pytest')


@pytest.mark.parametrize('search', ['pytest', 'python'])
def test_baidu_search_parametrize(search):
    """
    测试访问百度首页搜素pytest项目的内容
    这里需要用到request包
    :return:
    """
    # 发送请求
    x = requests.get('https://www.baidu.com/s?ie=utf-8&wd=' + search)

    # 返回 http 的状态码
    assert x.status_code == 200
    # 返回网页内容 是否包含 pytest
    assert str(x.text).find(search)


if __name__ == '__main__':
    pytest.main(["-vs", "itf_demo.py"])
