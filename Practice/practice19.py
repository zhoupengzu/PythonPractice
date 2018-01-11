# 匹配0次1次或者多次
# * 表示匹配*之前的字符0次或者无限多次
# + 表示匹配一次或者无数多次
# ? 表示匹配0次或者一次

import re

a = 'pytho0python1pythonn2'

print(re.findall('python+', a))  # ['python', 'pythonn']
print(re.findall('python*', a))  # ['pytho', 'python', 'pythonn']
print(re.findall('python?', a))  # ['pytho', 'python', 'python']
print(re.findall('python{1,2}?', a))  # ['python', 'python']
print(re.findall('\w{6,8}', a))  # ['pytho0py', 'thon1pyt']
print(re.findall('\d{4,5}', '100001'))
