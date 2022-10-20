#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: skip_xfail.py
@date: 2022/10/9 
"""
import sys

import pytest


@pytest.mark.skip(reason="no way of currently testing this")
def test_the_unknown():
    print("被跳过的测试")


def test_function():
    if not 1 == 2:
        pytest.skip("此表达式成立，将跳过")


@pytest.mark.skipif(sys.version_info < (3, 7), reason="requires python3.7 or higher")
def test_function_skipif():
    print("当你安装的python 版本小于3.7时，将提示你需要升级")


@pytest.mark.skipif(sys.platform == "win32", reason="does not run on windows")
class TestPosixCalls:
    def test_function_class(self):
        "will not be setup or run under 'win32' platform"


# xfail

@pytest.mark.xfail
def test_function_xfailed():
    print(1 / 0)


@pytest.mark.xfail
def test_function_xpassed():
    print(1 / 1)


if __name__ == '__main__':
    print(sys.version_info)
    pytest.main(['-rxXS', 'skip_xfail.py'])
