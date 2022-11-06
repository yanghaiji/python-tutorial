#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: dependency_demo.py
@date: 2022/11/3 
"""
import pytest


@pytest.mark.dependency()
def test_01():
    assert False


@pytest.mark.dependency(depends=["test_01"])
def test_02():
    print("执行测试2")


if __name__ == '__main__':
    pytest.main(["-vs", "dependency_demo.py"])
