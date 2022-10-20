#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: skip_xfail.py
@date: 2022/10/9 
"""
import pytest

xfail = pytest.mark.xfail


@xfail
def test_hello():
    assert 0


@xfail(run=False)
def test_hello2():
    assert 0


@xfail("hasattr(os, 'sep')")
def test_hello3():
    assert 0


@xfail(reason="bug 110")
def test_hello4():
    assert 0


@xfail('pytest.__version__[0] != "17"')
def test_hello5():
    assert 0


def test_hello6():
    pytest.xfail("reason")


@xfail(raises=IndexError)
def test_hello7():
    x = []
    x[1] = 1


if __name__ == '__main__':
    pytest.main(['-rxXS', 'skip_xfail02.py'])
