# coding=utf-8
class Student:
    def __init__(self,name,age):
        self.__name = name  #加了双下划线后在外部无法访问
        self.__age = age

    def set_name(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self,age):
        self.__age = age

stu = Student("zhoupengzu",10)
# stu.name    #访问不到
stu.set_name("change")
print stu.getName()