#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: parametrize.py
@date: 2022/10/9 
"""
import pytest


@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [("3+5", 8), ("2+4", 6), pytest.param("6*9", 42, marks=pytest.mark.xfail)],
)
def test_eval2(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("x", [0, 1])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print("------------")
    print("x = ", x)
    print("y = ", y)


if __name__ == '__main__':
    pytest.main(['-s', 'parametrize.py'])
