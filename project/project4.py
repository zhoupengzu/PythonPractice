'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''

import string

str1 = string.ascii_lowercase
alpha_list = list(str1)


def print_rangoli(size):
    rows = 2 * size - 1
    cols = 2 * size - 1 + 2 * (size - 1)
    all_str_list = []
    mid = rows // 2
    end_index = size
    for row in range(rows):
        if row <= mid:
            mid_str = "-" + alpha_list[size - row - 1] + "-"
            right_list = alpha_list[end_index - row:end_index]
            right_str = "-".join(right_list)
            left_str = right_str[::-1]
            all_str_list.append(left_str + mid_str + right_str)
        else:
            mid_str = "-" + alpha_list[row - mid] + "-"
            begin_index = row - mid + 1
            right_list = alpha_list[begin_index: size]
            right_str = "-".join(right_list)
            left_str = right_str[::-1]
            all_str_list.append(left_str + mid_str + right_str)

    for item in all_str_list:
        print(item.center(cols,"-"))

print_rangoli(1)
    
            





