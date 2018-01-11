
from itertools import combinations

origin_list1 = ['11','11','11','11','11']
change_list1 = list(combinations(origin_list1, 2))  # 该方法可以将一个可遍历对象分解成不同的元祖，元祖的长度就是函数的第二个参数
print(len(change_list1))

length = 10
elements = ['a', 'z', 'e', 'i', 'o', 'a', 'f', 'g', 'h', 'k'] #['a', 'a', 'c', 'd']
index = 5
index_indice = 'a'

elements = list(combinations(elements, index))
print(len(elements))
if len(elements) == 0:
    print(0)
else:
    find_count = 0
    # 方法一
    filter_obj = filter(lambda c: index_indice in c, elements)
    print(len(list(filter_obj)))  # 该列表的个数就是查找到的
    # 方法二
    for ele in elements:
        if index_indice in ele:
            # print(ele)
            find_count += 1
    answer = find_count / len(elements)
    print(answer)
