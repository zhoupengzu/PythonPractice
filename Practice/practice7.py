# 变量作用域
# python里面没有块级作用域  
# 只有函数才能形成一个作用域

c = 10
def scope():
    for x in range(1, 5, 2):
        a = 'a'
        for y in range(4, 1, -2):
            b = 'b'
    #正常来说，下面的应该是打印不出来的，但实际情况是它打印出来了
    print(a) # a
    print(b) # b

scope()
