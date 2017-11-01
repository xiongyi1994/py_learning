#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 列表生成器

# 生成[1*1,2*2,3*3...9*9]
list1 = [x*x for x in range(1,10)]
print(list1)

# 生成[2*2,4*4,6*6,8*8]
list2 = [x*x for x in range(1,10) if x % 2 == 0]
print(list2)

# 全排列 生成"ABC" 和 "XYZ"的全排列
list3 = [n + m for n in "ABC" for m in "XYZ"]
print(list3)

# 列出当前目录下的所有文件和目录名
import os
list_dir = [d for d in os.listdir('.')]
print(list_dir)