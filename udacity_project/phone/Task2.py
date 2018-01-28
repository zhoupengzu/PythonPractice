"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
任务2: 哪个电话号码的通话总时间最长? 不要忘记，用于接听电话的时间也是通话时间的一部分。
输出信息:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".

提示: 建立一个字典，并以电话号码为键，通话总时长为值。
这有利于你编写一个以键值对为输入，并修改字典的函数。
如果键已经存在于字典内，为键所对应的值加上对应数值；
如果键不存在于字典内，将此键加入字典，并将它的值设为给定值。
"""
phone_time_dic = {}

def add_phone_time(t=0, *phones):
    for phone in phones:
        if phone in phone_time_dic:
            phone_time_dic[phone] = phone_time_dic[phone] + t
        else:
            phone_time_dic[phone] = t


for call_info in calls:
    add_phone_time(int(call_info[-1]),*[call_info[0], call_info[1]])

phone_time_dic = {value:key for key,value in phone_time_dic.items()}
phone_time_list = phone_time_dic.keys()
phone_time_list = sorted(phone_time_list, reverse=True)
phone_time_list = list(phone_time_list)
max_long_time = phone_time_list[0]
result = "{phone} spent the longest time, {use_time} seconds, on the phone during September 2016.".format(
    phone=phone_time_dic[max_long_time], use_time = max_long_time)
print(result)

