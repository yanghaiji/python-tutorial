#!/usr/bin/env python
# coding=utf-8

"""
<p>入门案例
</p>
@author: hai ji
@file: test_sample.py
@date: 2022/9/30 
"""
import pytest


def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5


if __name__ == '__main__':
    pytest.main()