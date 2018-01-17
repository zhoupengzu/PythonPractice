'''
Given an integer, , print the following values for each integer  from  to :

Decimal
Octal
Hexadecimal (capitalized)
Binary
The four values must be printed on a single line in the order specified above for each  from  to . Each value should be space-padded to match the width of the binary value of .
'''

def print_formatted1(number):
    # 先计算二进制宽度
    bin_num = bin(number) # 如果用这种方法，则还需要把前缀截取
    print(bin_num)  # 0b10001
    print('%x' % (number)) # 11 # 该方式没办法输出二进制，所以放弃
    # format方法
    print('{0:b}'.format(number))  # 10001 可以发现该方法打印的结果不带0b之类的，这里的0表示第0个参数，第二个参数b表示二进制

'''
format的使用：可以使用数字来代表参数的位置，也可以用可变参数来指定，但是无论如何都需要用大括号包起来，如下面的0和width
'''
def print_formatted2(number):
    width = len("{0:b}".format(number))
    for num in range(1,number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(num, width = width))

print_formatted2(17)
