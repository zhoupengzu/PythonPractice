# coding=utf-8
"""
利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
"""
def upperStr(str):
    return str.upper()
def capitalizeStr(str):
    return str.capitalize()
def changeNameInRule(list):
    upper_list = map(upperStr, list)
    result_list = map(capitalizeStr, upper_list)
    return result_list

list = ['adam', 'LISA', 'barT']

print changeNameInRule(list)