# 变量作用域
# python里面没有块级作用域  
# 只有函数才能形成一个作用域
# 作用域都是相对来说的

c = 10
def scope():
    # c = c +1  #这里不能修改全局变量
    global c  # 要使用该相对来说的全局变量，则需要提前使用global修饰，然后才能修改其值
    c = c + 1
    for x in range(1, 5, 2):
        a = 'a'
        for y in range(4, 1, -2):
            b = 'b'
    #正常来说，下面的应该是打印不出来的，但实际情况是它打印出来了
    print(a) # a
    print(b) # b

scope()
print(c)


def func1():
    c = 10
    def func2():
        global c
        c = c + 2
    func2()
func1()
