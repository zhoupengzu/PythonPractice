# 正则替换：sub，通过控制最后一个参数count来控制替换的个数，默认为0，表示全部替换;
# 第二个参数可以为一个函数，也可以为要替换成的内容，当返回内容为空的时候，默认替换为空字符串

import re

def convert(value):
    print(value)  # <_sre.SRE_Match object; span=(0, 2), match='C#'>
    print(value.group())  # C# 获取匹配到的值
    return "Function"


language = 'C#PythonC#JavaC#PHP'

print(re.sub('C#', "Go", language))  # GoPythonGoJavaGoPHP
language = re.sub('C#', "Go", language, 2)
print(language)  # GoPythonGoJavaC#PHP

language = language.replace('Go', 'C#')
print(language)  # C#PythonC#JavaC#PHP
language = re.sub('C#', convert, language, 1)
print(language)  # 当什么都不返回的时候，打印PythonJavaPHP，当返回为Function时，打印为FunctionPythonC#JavaC#PHP

