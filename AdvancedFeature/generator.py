#/usr/bin/env python3
# -*- coding: utf-8 -*-

# 创建生成器的第一种方法 将列表生成器的[]改成为()
g = (x * x for x in range(10))
print(g)
print(next(g)) # -> 0
print(next(g)) # -> 1

for n in g:
    print(n)

# 创建生成器的第二种方法
# 如果一个函数定义中包含yield关键字，那么这个函数就不是一个普通的函数，而是一个generator

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n=n+1
    return 'done'

for n in fib(6):
    print(n)