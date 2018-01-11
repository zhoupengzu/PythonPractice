# 数量词
# 字符集只能匹配一个字符，如果要想匹配到一个字符串，则需要结合数量词

import re
a = 'python 1111java 678php+'

print(re.findall('[a-z]{3}', a))  # ['pyt', 'hon', 'jav', 'php']
print(re.findall('[a-z]{3,6}', a))  # ['python', 'java', 'php']
