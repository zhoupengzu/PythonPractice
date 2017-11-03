# coding=utf-8
print "============================================数字========================================="
define_number = 2    #创建一个数字对象
print "我是新定义的数字对象：",
print define_number
#del语句用来删除对象引用，删除后再使用就会报错(下面就会报错)，删除多个，对象之间用逗号分隔开就好
"""
del define_number
print "我是del后的：",
print define_number

"""

#定义一个复数
define_complex = 2 + 3.8j
print define_complex
