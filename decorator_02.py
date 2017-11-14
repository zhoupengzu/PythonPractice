# coding=utf-8
#不带参数的装饰器
def log(func):
    def wrapper(*args,**kw):
        print "call %s()" % func.__name__
        return func(*args,**kw)
    return wrapper

#带参数的装饰器
def log(text):
    def decorator(func):
        print "%s %s()" % (text,func.__name__)
        return func
    return decorator
@log("execute")
def testDecorator():
    print "hahahhahahhahhahahha"
testDecorator()
print testDecorator.__name__