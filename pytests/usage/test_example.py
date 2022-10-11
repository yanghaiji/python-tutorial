#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: test_example.py
@date: 2022/10/5 
"""
import pytest


@pytest.fixture
def error_fixture():
    assert 0


def test_ok():
    print("ok")


def test_fail():
    assert 0


def test_error(error_fixture):
    pass


def test_skip():
    pytest.skip("skipping this test")


def test_xfail():
    pytest.xfail("xfailing this test")


@pytest.mark.xfail(reason="always xfail")
def test_xpass():
    pass


if __name__ == '__main__':
    pytest.main(["-rfs", "test_example.py"])
