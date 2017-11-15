# coding=utf-8

'''
使用type方法来判断对象类型
'''

print type(123)


class Student:
    def __init__(self):
        pass


stu = Student()
# print type(stu)
print dir('abc')  #打印字符串的所有方法
print 'abc'.__len__()   #len('abc')内部也是去调用这个方法
# print dir(stu)

# getattr()、setattr()以及hasattr()用来给某个属性设置值或者获取值或者判断是否有这个属性