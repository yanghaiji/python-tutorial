#!/usr/bin/env python
# coding=utf-8

"""
<p>

</p>
@author: hai ji
@file: strings.py
@date: 2022/9/19 
"""

if __name__ == '__main__':
    str1: str = "hello world"
    str2: str = 'hello python'
    print("str1 的值为：%s" % str1)
    print("str2 的值为：%s" % str2)
    # 当字符串过长时
    str3 = "4s5dyunlkmvo;udznv b,hbvaliygwj khjdeuibnjkm" \
           "suyvaj czlkj z,vkj ,j jdshbfabewkafyaiesatwet"
    # 字符串过长时，且想保留字符串原有的格式时
    str4 = """这是一个很长的字符串，
    我想在实用时，保留其原有的格式！
    """
    print("str3 的值为：%s" % str3)
    print("str4 的值为：%s" % str4)

    # 当字符串内有单引号时，我们外层可以使用双引号，反之亦然
    str5 = "It's My Turn"
    print("str5 的值为：%s" % str5)
    # 当字符串内有 \ / 且我们需要保留原有的格式时,
    # 如果不添加 \ 则会将\n解析成回车
    str6 = "C:\python\\name"
    print("str6 的值为：%s" % str6)
    str7 = r"C:\python\name"
    print("str7 的值为：%s" % str7)

    str7 = "st7"
    str8 = "str8"
    str9 = str8 + str7
    print("str9 的值为：%s" % str9)

    # 数据切片 这里的数据下标是从0开始
    str10 = "0123456789"
    print("str10[3] 的值为：%s" % str10[3])
    # [3:8] 的表达式遵循左闭又开的原则
    print("str10[3] 的值为：%s" % str10[3:8])
    # str10[0] = 's'

    # replace
    str_rep = "Python"
    str_rep = str_rep.replace('o', 'O')
    print("str_rep 的值为：%s" % str_rep)

    lower = str_rep.lower()
    print("lower 的值为：%s" % lower)

    index_num = lower.index("o")
    index_num2 = lower.index("o", 2)
    index_num3 = lower.index("o", 2,len(lower))
    print("index_num 的值为：%s" % index_num)
    print("index_num2 的值为：%s" % index_num2)
    print("index_num3 的值为：%s" % index_num3)
