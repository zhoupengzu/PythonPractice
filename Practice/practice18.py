# 贪婪和非贪婪，默认是贪婪的，主要用于数量词，当限定取值个数范围后，会取尽可能多的字符，非贪婪则需要在数量词后添加一个？号

import re
a = 'python 1111java 678php+'

print(re.findall('[a-z]{3}', a))  # ['pyt', 'hon', 'jav', 'php']
print(re.findall('[a-z]{3,6}', a))  # ['python', 'java', 'php']
print(re.findall('[a-z]{3,6}?', a))  # ['pyt', 'hon', 'jav', 'php']
