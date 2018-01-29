# 将任何的字符串，将其中的大写字母改为小写，小写字母改为大写的

'''
isalnum(),isalpha(),isdigit(),islower(),isupper()
import textwrap
textwrap.wrap(str, width=70)
textwrap.fill(str, width=70)
'''
def swap_case(s):
    result = ""
    # 方法一：遍历，重新组装
    for c in s:
        if c.islower():
            result += c.upper()
        else:
            result += c.lower()
    print(result)
    # 方法二：直接调用内置方法swapcase()
    print(s.swapcase())

swap_case("Hello,World")
