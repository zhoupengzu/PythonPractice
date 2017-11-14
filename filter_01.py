# coding=utf-8
import math
"""
和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
"""
def is_odd(n):
    return n % 2 == 1
list = range(0,10,1)
print filter(is_odd,list) #[1, 3, 5, 7, 9]

#利用生成器生成1到100，并筛选出其中的素数（质数）
def deleteSuShu(value):
    isSpecial = True
    if value == 1:
        isSpecial = False
        return isSpecial
    if value > 1:
        for index in range(2, (int)(math.sqrt(value)) + 1):
            if value % index == 0:
                isSpecial = False
                break
    return isSpecial
list = (value for value in range(1,101))
print filter(deleteSuShu,list)