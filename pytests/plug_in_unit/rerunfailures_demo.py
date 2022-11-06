#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: rerunfailures_demo.py
@date: 2022/11/3 
"""

import pytest


@pytest.mark.parametrize('a,b,result', [
    (1, 1, 3),
    (2, 2, 4),
    (100, 100, 200),
    (0.1, 0.1, 0.2),
    (-1, -1, -2)
], ids=['int', 'int', 'bignum', 'float', 'fushu'])  # 参数化
@pytest.mark.flaky(reruns=6, reruns_delay=2)
def test_add(a, b, result):
    # cal = Calculator()
    assert result == a + b


if __name__ == '__main__':
    # "--reruns 5 --reruns-delay 1",
    pytest.main(['-vs', "rerunfailures_demo.py", "-n 2"])
