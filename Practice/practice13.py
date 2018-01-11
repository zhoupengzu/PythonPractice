
# def func_args(**kwds, * args): 关键字可选参数不能在可选参数之前
def func_args(*args, **kwds):
    print(args)
    print(kwds)
    print(kwds.get('repeat',10))

func_args(*[1, 2, 3], 'ABC')
print('==========================')
func_args(*[1,2,3], 'ABC',repeat=1)
