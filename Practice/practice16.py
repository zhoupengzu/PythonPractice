# 概括字符集，如\d、\D

import re

a = 'pytho\n_1111java 678php+'
# 查找其中的数字
print(re.findall('\d', a))
print(re.findall('[0-9]', a))
# 查找其中的非数字
print(re.findall('\D', a))
print(re.findall('[^0-9]', a))
# 数字和字母和下划线
print(re.findall('\w', a))
print(re.findall('[A-Za-z0-9_]', a))
# \W(\w的反面)
print(re.findall('\W', a))
# \s,\S
print(re.findall('\s', a))
# . 匹配除换行符（\n）外的字符
print(re.findall('.', a)) #['p', 'y', 't', 'h', 'o', '_', '1', '1', '1', '1', 'j', 'a', 'v', 'a', ' ', '6', '7', '8', 'p', 'h', 'p', '+'] 
