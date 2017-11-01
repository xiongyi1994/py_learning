#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 判断一个对象是否可以迭代
from collections import Iterable
print(isinstance("abc",Iterable)) # -> true

# 迭代输出
for value in "abc":
    print(value)

# 迭代输出下标 enumerate()函数
for i,value in enumerate("abc"):
    print(i,value)