
from functools import reduce

a1_s = [2]
a1 = [1,2,3,4,5,6,7,8,9,0]

r1_s = reduce(lambda x,y: x+y,a1_s)
print(r1_s)  # 2
r1 = reduce(lambda x,y: x+y, a1)
print(r1)

r1_1 = reduce(lambda x,y: x+y,a1,5)
print(r1_1)
