# 类
'''
1、使用关键字class定义，类名后添加括号，括号中是继承的类
2、__init__是该类的构造函数，且构造函数只能哦鱼一个
3、所有的构造函数的第一个参数都是self
4、实例变量和类变量，在查找时，如果实例变量没有定义，就会去类变量中查找，如下面的height，是个类变量
5、可以使用__dict__来查看实例对象和类所拥有的变量
6、如果用类名调用实例方法，则需要显式的传入对象，如下面的Person.print_info(person2)使用
'''
class Person():
    height = 160  #这是类变量
    name = 'default'
    # def __init__(self, name):
    #     self.name = name    
    def __init__(self, name, age):
        self.name = name  #这是实例变量
        self.age = age
        print(name)  # zhou 
    def print_info(self):
        print('name:', self.name,',age:', self.age, ',height:', self.height)
    
# person1 = Person('zhou')
person2 = Person('zhou', 20)
person2.print_info()
Person.print_info(person2)
print(person2.__dict__)  # {'name': 'zhou', 'age': 20}
print(Person.__dict__)
print(Person.print_info)
