# 序列解包与链式赋值
'''
 str,tuple,list,set,dict都可以做序列解包和赋值，但是需要注意：
 1、dict得到的是其key
 2、两边的个数需要相同
'''
a = 1, 2, 3
print(type(a))  #<class 'tuple'>
print(a) #(1, 2, 3)

# a, b = 1, 2, 3  #这样是不行的
# a, b, c = 1, 2  #这样也是不行的

a, b, c = (1,2,3)
print(a,b,c)

a, b, c = [1,2,3]
print(a,b,c)

a,b,c = 'abc'
print(a, b, c)

a,b,c = {1,2,3}
print(a,b,c)

a,b,c = {'1':1,'2':'2','3':'c'}
print(a, b, c)  # 1 2 3

