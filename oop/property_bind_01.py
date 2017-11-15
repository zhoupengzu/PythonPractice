# coding=utf-8


class Person(object):
    def __init__(self):
        self.__score = 0

    @property
    def score(self):
        print "get"
        return self.__score

    @score.setter
    def score(self, score):
        print "set"
        if isinstance(score, int):
            self.__score = score
        else:
            raise ValueError('not a int value')


per = Person()
per.score = 200
print per.score
# per.score = "a"
