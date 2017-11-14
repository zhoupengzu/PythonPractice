# coding=utf-8
# 迭代
from collections import Iterable
dic = {'a': 1, 'b': 2, 'c': 3}
# 下面直接打印的是key
for key in dic:
    print key
print "################################"
for key in dic.iterkeys():
    print key
print "################################"
# 下面打印的是value
for value in dic.itervalues():
    print value
print "################################"
for item in dic.iteritems():  # 这样返回的item是一个元祖，括号可不加
    (key, value) = item
    print key, '=', value

print "对象是否可迭代"
if isinstance(dic, Iterable):
    print "dic是可迭代对象"
else:
    print "dic不是可迭代对象"
