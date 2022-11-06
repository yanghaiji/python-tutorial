#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: assume_demo.py
@date: 2022/11/3 
"""
import pytest


def test_assume():
    print('登录操作')
    pytest.assume(1 == 2)
    print('搜索操作')
    pytest.assume(2 == 2)
    print('加购操作')
    pytest.assume(3 == 2)


if __name__ == '__main__':
    pytest.main(["-vs", "assume_demo.py"])
