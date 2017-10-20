#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 构造函数
list_con = list('abc')
print(list_con) # -> ['a', 'b', 'c']

# len 长度
print(len(list_con)) # -> 3

# append 添加在末尾
list_con.append('d')
print(list_con) # -> ['a', 'b', 'c', 'd']

# insert 添加在索引位置
list_con.insert(1,'xiongyi')
print(list_con) # -> ['a', 'xiongyi', 'b', 'c', 'd']

# pop 删除末尾元素
list_con.pop()
print(list_con) # -> ['a', 'xiongyi', 'b', 'c']

# sort
list_sort = list('1324123412')
print(list_sort)
