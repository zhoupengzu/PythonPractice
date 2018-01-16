# 字典的推导式

a1 = [1,2,3,4,5]
print(tuple(a1))

a2 = {'name':'zhou','age':20}
r2 = [key for key, value in a2.items()]  # 和[key for key in a2]等价
print(r2)
r2_2 = (key for key, value in a2.items())
print(r2_2)  # <generator object <genexpr> at 0x104c2df68>
