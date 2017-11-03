# coding=utf-8
a = 10
b = 20
c = a

if c is a:
    print "a and c is same pointer"
else:
    print "a and c is not same pointer"

if b is c:
    print "b and c is same pointer"
elif b is a:
    print "b and a is same pointer"
else:
    print "找不到"
#改变了之后，就不会再相同了
a = 20
print c
if a is not c:
    print "a and c is not same any more"