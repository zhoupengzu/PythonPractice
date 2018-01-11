# 正则表达式，使用的库为re;是由元字符（如'\d'）和普通字符(字符串)组成的

import re

# 查找字符串中的Python
# 方法一
a = 'C|C++|Java|C#|Python|Javascript'
reg = re.findall('Python', a)
print(reg)
# 方法二：
a.index('Python')
# 方法三：
if 'Python' in a:
    print('包含')
# 方法四：


'''
 提取其中的字符0
 正则表达式：\d 表示数字，匹配一个数字；
    \D 表示非数字
 '''
a1 = 'C0C++1Java0C#3Python5Javascript'
print(re.findall('\d', a1))
