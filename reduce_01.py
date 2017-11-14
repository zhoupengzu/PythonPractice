# coding=utf-8
"""
reduce接受两个参数，使用和map相同，但是reduce中的函数必须要传递两个参数
"""
def sum(x,y):
    return x + y
list = range(1,5)
print reduce(sum,list) #10