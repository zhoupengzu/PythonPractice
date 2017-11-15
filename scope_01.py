# coding=utf-8
'作用域'
__author__ = "zhoupengzu"

def _greeting(name):
    print "Hello,%s" % name
def __specialGreeting(name):
    print "我想死你了,%s" % name
def nomalGreeting(name,isSpecial = False):
    if isSpecial:
        __specialGreeting(name)
    else:
        _greeting(name)
        