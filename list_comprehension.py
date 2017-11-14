# coding=utf-8
#列表生成式，通过列表生成式，可以直接创建一个列表
list = range(0,5,2)
print list,len(list)
#列表生成公式：1、中括号必须有；2、前面的x*x是生成额规则，x是列表元素；3、可以添加筛选条件，如power_condition
power = [x * x for x in range(1,5)]
print power
power_condition = [x * x for x in range(1,10) if(x % 2 == 0)]
print power_condition

list_product = [m + n for m in 'ABC' for n in 'abc']
print list_product