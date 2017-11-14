# coding=utf-8
#列表生成式
list = range(0,5,2)
print list,len(list)
#列表生成公式：1、中括号必须有；2、前面的x*x是生成额规则，x是列表元素
power = [x * x for x in range(1,5)]
print power

list_product = [m + n for m in 'ABC' for n in 'abc']
print list_product