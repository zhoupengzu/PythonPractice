# 匹配模式参数：findall的第三个参数,有多个值时，用“|”分割，表示且

import re

language = 'PythonC#\nPHPJava'
print(re.findall('c#', language))  # []
print(re.findall('c#', language, re.I))  # ['C#']
print(re.findall('c#.', language, re.I))  # []
print(re.findall('c#.', language, re.I | re.S))  # ['C#\n']
