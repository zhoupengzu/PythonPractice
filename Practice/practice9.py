'''
类方法、静态方法、成员可见性、继承、调用父类方法
1、可见性：默认的都是可见的，当以双下划线开头时，就变成了私有的；私有的都只能在类内部使用和访问
   但是要注意，不要在结束的时候再增加双下划线，一般以双下划线开头和结束的都是系统使用的
   如果要是在外部使用双下划线调用，则默认是给该对象添加了一个新的变量（如下面的human1的__school，不能在human2中使用）
2、类方法使用@classmethod定义，一般通过类名直接调用，也可以使用实例化对象调用，和变量是一样的
    在类方法中没办法直接调用实例化的方法和变量，可以初始化一个对象或者传入一个对象调用；但是在实例化方法中可以调用类方法和类变量
    可以通过__class__方法从实例化变量获取其类
3、静态方法使用@staticmethod定义，一般通过类名直接调用，也可以通过实例化对象调用，和变量一样
    静态方法和类方法、对象方法不同的是，它没有默认传入参数（如类方法的cls，对象方法的self），可以根据需要传参数，也可以不传
4、继承：在python里支持多继承
'''

import sys

class Human():
    # 类成员变量
    id_card = 'default'
    # 私有类成员变量
    __private_num = '0000'
    # 普通成员变量
    __normal_info__ = 'default'

    def __init__(self):
        self.name = "default"
        self.age = 0
        self.__school = ''
    def instance_method(self):
        print(self)
        self.class_method_1()
        self.__class__.class_method_1()

    def __private_instance_method(self):
        print('this is a private method')

    @classmethod
    def class_method_1(cls):
        print('This is a class method!')
        print(cls)  # <class '__main__.Human'>
        print(cls.__private_num)
        # print(cls.name) # 这句是错的，传进来的cls是类
        # cls.__private_instance_method()
    @classmethod
    def class_method_2(cls):
        print('This is a class method2')

    @staticmethod
    def static_method_1():
        print('This is a static method1')
    
    @staticmethod
    def static_method_2(self):
        print(self.name)
    
    @staticmethod
    def static_method_3(cls):
        print(cls)

    @classmethod
    def __private_class_method_1(cls):
        print('this is a private class method')

def local_practice():
    human1 = Human()
    human2 = Human()
    print('可见的：' + human1.id_card)
    # print('私有的：' + human1.__private_num) # 这里会报错：AttributeError: 'Human' object has no attribute '__private_num'
    print('系统使用：' + human1.__normal_info__)
    print(human1.id_card)  # 这里只是调用了类变量，并不是实例变量
    print(human1.__dict__)  # {'name': '', 'age': 0, '_Human__school': ''}
    human1.__school = 'new var'
    # {'name': '', 'age': 0, '_Human__school': '', '__school': 'new var'}
    print(human1.__dict__)
    # print(human2.__school) # AttributeError: 'Human' object has no attribute '__school'
    #类方法调用
    Human.class_method_1()
    Human.class_method_2()
    human1.class_method_1()
    human1.instance_method()

    if human1.__class__ == Human:
        print('equal')

    # 静态方法调用
    Human.static_method_1()
    human1.static_method_1()
    human1.static_method_2(human1)
    Human.static_method_2(human1)
    Human.static_method_3(human1)  # <__main__.Human object at 0x101f63978>
    Human.static_method_3(Human)  # <class '__main__.Human'>

args = sys.argv
if len(args) > 1:
    local_practice()