#/usr/local/env python3
# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self,name,sex,score):
        self.name = name # 实例属性
        self.sex = sex
        self.__score = score # 私有变量

student_a = Student('xiongyi','male',90)
print(student_a)


# 继承
class Student_extend(Student):
    pass


