# 边界匹配符
# 在之前用^(表示从字符串开始的地方匹配)在结束的地方使用$（在字符串末尾进行匹配）

import re

qq = '100000001'
print(re.findall('\d{4,9}', qq))
print(re.findall('^0{4}', qq))  # []
print(re.findall('^10{7}1$', qq))  # ['100000001']
print(re.findall('^10{7}$', qq))  # [] 因为此时不是以1结尾的
