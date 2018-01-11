# 字符集

import re

s = 'abc, acc, adc, aec, afc, ahc, acfc'

'''
找出上述字符串中中间字母是c或者f的单词
[] 匹配其中包含的单个字符，中间的字符是或的关系，即每次只匹配其中一个
^ 表示不是某个字符
a-b 表示从一个到另一个，即从a到b
'''
print(re.findall('a[cf]c', s))  # ['acc', 'afc']
print(re.findall('a[^cf]c', s))  # ['abc', 'adc', 'aec', 'ahc']
print(re.findall('a[a-d]c', s))  # ['abc', 'acc', 'adc']
