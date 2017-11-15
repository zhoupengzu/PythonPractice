# coding=utf-8


from types import MethodType


class Student:
    def __init__(self):
        pass


stu = Student()
stu.age = 20   # 添加了一个属性age并赋值为20
stu.score = 100

stu2 = Student()
stu2.score = 99


def get_age(self):
    return self.age


stu.get_age = MethodType(get_age, stu, Student)     # 添加了一个方法，但是该方法只能在stu中使用，其他新定义的Student的对象不能使用


def get_score(self):
    return self.score


Student.get_score = MethodType(get_score, None, Student)   # 添加一个方法，该方法所有的Student的实例对象都能使用
print stu.get_score()
print stu.get_age()

print stu2.get_score()
# print stu2.get_age()    # 会报错
