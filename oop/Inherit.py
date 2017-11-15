# coding=utf-8


class Animal:
    def __init__(self):
        pass

    def run(self):
        print "Animal is running"

    def duoTai(self, animal):  #多态
        animal.run()


class Dog(Animal):     #小括号里的表示继承的父类
    def eat(self):     #添加自己的方法
        print "dog is eatting"


class Cat(Animal):
    def run(self):    #重写父类的方法，调用的时候总是会优先调用该方法，即多态
        print "cat is running"
'''
错误写法
'''
    # def run(self,name):
    #     pass

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()

print isinstance(dog, Animal)

'多态测试'
dog.duoTai(dog)
cat.duoTai(cat)
