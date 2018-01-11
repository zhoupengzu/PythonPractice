# 组：使用小括号把一系列的字符括起来，表示要以小括号里的内容作为一个整体进行匹配

import re

a = 'pythonpythonpythonpython'
# 判断字符串中是否包含三个python
print(re.findall('(python){3}', a))  # ['python']
