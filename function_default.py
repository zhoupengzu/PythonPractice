# coding=utf-8
def power(x,n=2):
    return x**n;

result = power(2);
print result;
'''要注意下面的默认值'''
def attention(L=[]):
    L.append("error");
    return L;
attention();
attention();
print attention();
'''改成下面的就对了'''
def attention_new(L=None):
    if L is None:
        L = [];
    L.append("right");
    return L;
attention_new();
attention_new();
attention_new();
print attention_new();