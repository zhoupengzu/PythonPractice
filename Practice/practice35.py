# 综合练习
'''
1、切片的第三个参数控制了方向，前两个参数控制了开始和结束的位置
2、center(width,fill)当字符串的长度达不到width时，对字符串做居中并使用字符fill填充
'''
from practice35_func import sort_list
from functools import reduce
# 字符串
str1 = 'insert 0 5'
print(str1.split(' '))
print('center:')
str2 = 'hahaha'
print(str2.center(10,'*'))
print(str2.center(5,'='))

# 列表
list1 = []
list1.insert(2, 2)  # [2]
print(list1)
remove_value1 = 3
if remove_value1 in list1:  # remove之前需要先确定列表中是否存在。否则容易出错
    list1.remove(remove_value1)
elif 4 in list1:
    pass
print(list1)
print('list to str:')
print(str(list1)) 

# 平均数
print('平均数:')
scores = [52,56,60,99,80]
print(round(float(reduce(lambda x, y: x + y, scores)), 2))
print(('%.2f' % reduce(lambda x, y: x + y, scores)))  # 保留两位小数
print(scores[::-2])  
print(scores[:2:-1])
print(scores[::-1]) 
print('extend：')
list1.extend((2,5,4))
print(list1)
print('排序：')
list1.sort()
print(list1)
list1.pop()
print(list1)
# print(hash(list1)) # 不能被hash
print('students')
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
# students.sort(key=sort_list)
students.sort(key=lambda item: item[1])
print(students)
# print(students[10])


# 元祖
tuple1 = tuple(list1)
print(tuple1)
print(hash(tuple1))

# range
for n in range(3,0,-1):
    print(n)

