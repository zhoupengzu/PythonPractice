# coding=utf-8
def mutable(*numbers):
    sum = 0;
    for num in numbers:
        sum += num;
    return sum;

print mutable(2,3,4,5);
print mutable(2,3,4,5,6);
print mutable(2,3,4,5,7,8);
'''参数是list'''
list = [1,2,3,4];
print mutable(*list);