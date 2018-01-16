# 列表推导式
# filter

a1 = [1,2,3,4,5,6,7]

print(list(filter(lambda a: a > 5, a1)))

def filter_func(a):
    return a > 5

print(list(filter(filter_func, a1)))


# 列表推导式
r1 = [a**2 for a in a1 if a > 5]
print(r1)
