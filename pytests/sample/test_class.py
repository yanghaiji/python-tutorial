#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: test_class.py
@date: 2022/10/5 
"""


class TestClass:
    # 判断其是否存在包含的关系
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
