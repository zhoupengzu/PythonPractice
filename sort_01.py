# coding=utf-8
"""
排序算法，使用方法和map、reduce、filter相同，排序算法的方法必须传递两个参数；
更重要的是，可遍历对象要写在前面，然后是排序算法
"""
def reversed_cmp(x,y):
    if x > y:
        return -1
    elif x < y:
        return 1
    else:
        return 0

list = [36, 5, 12, 9, 21];
print sorted(list,reversed_cmp)