#/usr/local/env python3
# -*- coding: utf-8 -*-

class Student(object):
    pass

s = Student()

# 给实例绑定属性
s.name = 'xiongyi'
print(s.name)

# 给实例绑定方法
def set_age(self,age):
    self.age = age
from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(24)
print(s.age)

