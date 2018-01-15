# 可变参数练习

a1 = [1, 2, 3, 4]
a2 = [5,4,2,1,3]

def mutable_params(*args):
    print(args)
    print(type(args))


mutable_params(a1)  # ([1, 2, 3, 4],)
mutable_params(*a1)  # (1, 2, 3, 4)

mutable_params(a1, a2)  # ([1, 2, 3, 4], [5, 4, 2, 1, 3])
mutable_params(*a1, *a2)  # (1, 2, 3, 4, 5, 4, 2, 1, 3)

def mutable_params_2(a, b, *args):
    print(a),
    print(b),
    print(args)

mutable_params_2('name','age',a1)
mutable_params_2('name', a1)
mutable_params_2('name', a1,a2,'age')
