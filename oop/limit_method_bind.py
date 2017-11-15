# coding=utf-8

"""
限制属性绑定
通常情况下，我们可以动态的为类或者对象绑定任何需要的属性和方法
但是可以通过__slots__来限制属性的绑定
"""


class Person(object):
    __slots__ = ('name',)  # 允许绑定的属性,__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的，比如子类中的age


person = Person()
person.name = "person"
# person.age = 20  # 这里会报错，前提是Person继承object，否则slots不起作用


class Student(Person):
    __slots__ = ('name', 'score')  # 如果添加了这一行，则可允许的动态添加属性是子类的slots和父类的slots的并集，因为父类和子类都没有加age，所以这里的age会报错

    def __init__(self):
        pass


stu = Student()
stu.name = "哈哈"
stu.age = 20   # 打开了自己的slots后会报错
print dir(stu)
