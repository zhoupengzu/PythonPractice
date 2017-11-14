# coding=utf-8
"""
在代码运行期间，动态增加功能的方式，成为装饰器，使用@符号，把decorator放到需要观察的方法或者变量的定义处即可
__name__可以打印出当前调用函数的名字
"""
def now():
    print "__name__"
print now.__name__

#装饰器
def log(func):
    def wrapper(*args,**keyword):
        print "call %s()" % func.__name__
        return func(*args,**keyword)
    return wrapper

@log
def decorator():
    print "I am a decorator"

decorator() #这里相当于执行了decorator=log(decorator)
print decorator.__name__  #wrapper