# lambda（匿名函数）和三元表达式
# 对于map来说，当传入多个可遍历的对象时，以最短的为准

a1 = [1,2,3 ,4]
a2 = [[1,2],[3],[4,5,6]]
a3 = [4,2,1,3]
# 将数组里的每一个元素都平方
r1 = map(lambda x: x*x, a1)
print(list(r1))  # [1, 4, 9, 16]
# r2 = map(lambda x: x*x, *a2)
# print(list(r2))

r3 = map(lambda x,y: x + y, a1, a3)
print(list(r3))  # [5, 4, 4, 7]

# 三元表达式
x = 10
y = 20
l1 = x if x > y else y
print(l1)  # 20
