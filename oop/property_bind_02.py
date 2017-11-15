# coding=utf-8

"""
这里只定义了只读属性
"""


class Person(object):
    __slots__ = ('__score',)

    def __init__(self):
        self.__score =20

    @property
    def score(self):
        return self.__score


per = Person()
# per.score = 20  # AttributeError: can't set attribute没有定义set属性
print per.score
