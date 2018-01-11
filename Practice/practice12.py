# list1 = [1, 2, 4, 2]
# print(max(list1))

from itertools import product
# product 用于求多个可迭代对象的笛卡尔积，它跟嵌套的 for 循环等价
list1 = ['A', 'B', 'C']  # [('A', 'B', 'C')]
print(list(product(*list1)))
# print(list1)
print(list(product(*list1,'XYZ'))) # [('A', 'B', 'C', 'X'), ('A', 'B', 'C', 'Y'), ('A', 'B', 'C', 'Z')]
list2 = [['A', 'B'], ['C', 'D'], 'E'] # [('A', 'C', 'E'), ('A', 'D', 'E'), ('B', 'C', 'E'), ('B', 'D', 'E')]
print(list(product(*list2)))
print(list(product(*list2, 'XYZ')))
# product(*list2, repeat=2)和product(*list2, *list2)相同

# print(tuple({'A':1}))

str1 = '''2 488512261 423332742
2 625040505 443232774
1 4553600
4 92134264 617699202 124100179 337650738
2 778493847 932097163
5 489894997 496724555 693361712 935903331 518538304'''

list_count, module_num = [6, 767]
list_array = []
list_element = str1.split('\n')
# print(list_element)
for lists in list_element:
    temp_lists = list(map(lambda num: int(num), lists.split(' ')))
    list_array.append(temp_lists[1:])
# print(list_array)
# print(list(product(*list_array))[8])  # (7, 7, 7, 7, 7, 8518829, 7)
results = map(lambda x: sum(i**2 for i in x) % module_num, product(*list_array))
print(max(list(results)))

# 下面的方法也可以
# new_list_array = list(product(*list_array))
# result = 0
# for item in new_list_array:
#     temp_sum = 0
#     for in_item in item:
#         temp_sum = temp_sum + in_item**2
#     if(temp_sum % module_num > result):
#         result = temp_sum % module_num
        
# print(result)
