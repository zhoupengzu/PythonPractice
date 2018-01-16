# 装饰器

import time

def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper

@decorator
def decorator_use_1():
    print('decorator_use_1')

@decorator
def decorator_use_2(name, age):
    print('decorator_use_2')


decorator_use_1()
    
decorator_use_2('name','age')
