# coding=utf-8

"""
多重继承
除了单一继承的外，再继承其他的，这种设计称为Mixin
"""


class Animal(object):
    pass


# 哺乳类
class Mammal(Animal):
    pass


# 鸟类
class Bird(Animal):
    pass


# 会跑的
class RunnableMixin(object):
    def run(self):
        print ("Running...")


# 会飞的
class FlyableMixin(object):
    def fly(self):
        print ("Flying...")


# 各种动物
# 狗即是哺乳类也会跑
class Dog(Mammal, RunnableMixin):
    pass


# 鹦鹉是鸟类也会飞
class Parrot(Bird, FlyableMixin):
    pass
