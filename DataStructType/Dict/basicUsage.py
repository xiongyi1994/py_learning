#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dict的特点

dict_dir = {'name':'xiongyi','age':23}
print(dict_dir)

# get 得到某个key的vale
print(dict_dir.get('name')) # -> xiongyi

# pop 删除某个key
dict_dir.pop('age')
print(dict_dir)