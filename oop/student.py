# coding=utf-8
"""
只能有个一个构造函数
"""
class Student:
    def __init__(self,name,score):
        self.name = name
        self.score = score
    # def __init__(self):
    #     self.name = "default"
    #     self.score = 0
    def printStuInfo(self):
        print "姓名：%s,分数：%s" % (self.name, self.score)

stu = Student("zhoupengzu",99)
print "姓名：%s,分数：%s" % (stu.name,stu.score)
stu.printStuInfo()