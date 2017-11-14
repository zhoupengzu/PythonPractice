# coding=utf-8
'''
map接受两个参数，一个是函数，一个是序列
map将传入的函数依次作用到序列的每个元素上
'''
def power(n):
    return n * n
list = range(1,10)
print list
list = map(power,list)
print list