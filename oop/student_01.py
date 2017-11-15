# coding=utf-8
class Student:
    def __init__(self,name="default",score=0):
        self.name = name
        self.score = score

stu1 = Student("zhou",20)
stu2 = Student("zpz",30)
"""
这个时候stu1和stu2拥有同样的属性name和score
"""
stu1.age = 18
"""
这个时候stu2是没有age属性的，访问会报错
"""
# print stu2.age
print stu1.age
'判断stu1和stu2是否指向同一个对象'
if stu1 is stu2:
    print "same"
else:
    print "different"