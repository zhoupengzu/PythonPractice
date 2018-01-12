# 枚举
# 该特性是在python3中才有的
'''
注意事项：
1、必须初始化
2、不同的变量的类型可以为不同的类型
3、一旦有了值，就不能再改变
4、必须使用value和name获取对应的枚举值和枚举名
5、枚举之间不能做大小比较，但是可以做是否相等比较

为什么不实用字典、类、变量等定义枚举？
1、其值容易被改变
2、不能保证其唯一性
'''

from enum import Enum

class Colors(Enum):
    GREEN = 1
    YELLOW = '1'
    BLUE = 2

# Colors.GREEN = 2
enum1 = Colors.GREEN
print(enum1) # Colors.GREEN
print(type(enum1))  # <enum 'Colors'>
print('name:' + enum1.name + ',value:' +
      str(enum1.value))  # name:GREEN,value:1

# 不能做大小比较
# if Colors.GREEN < Colors.BLUE:
#     print('small')
# else:
#     print('not small')

# 可以做是否相等的比较
if Colors.GREEN == Colors.BLUE:
    print('equal')
else:
    print('not equal')
