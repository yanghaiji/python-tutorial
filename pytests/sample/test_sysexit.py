#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: test_sysexit.py
@date: 2022/10/5 
"""
import pytest


def f():
    # 请求退出解释器
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()


if __name__ == '__main__':
    pytest.main(["test_sysexit.py"])
