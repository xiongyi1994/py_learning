# -*- coding:utf-8 -*-

'''
	redis string 可以存储三种类型的值 字节串、整数、浮点数
'''


import redis
conn = redis.StrictRedis(host='localhost', port=6379, db=0)

# set
conn.set("string-key1","xiongyi")

# get
conn.get("string-key1") # => xiongyi

# del
conn.delete("string-key1")

# incr
conn.set("incr_ex_int", 1)
conn.incr("incr_ex") # => 2

conn.set("incr_ex_float", 1.0)
#conn.incr("incr_ex_float") # => error info: value is not an integer or out of range

conn.set("incr_ex_string_1", "1")
conn.incr("incr_ex_string_1") # => 2

conn.set("incr_ex_string_2", "a")
#conn.incr("incr_ex_string_2" # => error info: value is not an integer or out of range

# decr
# same as incr

# incrby
conn.set("incrby_ex",1)
conn.incrby("incrby_ex",2) # -> 3

# decrby
# same as incrby

# incrbyfloat

# append
conn.set("append_ex", "xiong")
conn.append("append_ex", "yi") # => xiongyi

# getrange
conn.set("getrange_ex", "012345")
conn.getrange("getrange_ex", 0, -1) # => 012345

# setrange

# getbit

# setbit

# bitcount

# bitop
