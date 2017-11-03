# coding=utf-8
define_str = "我是一个字符串"
print define_str
#字符串索引从左到右，是从0开始
#从右到左，索引是从-1开始
#【beginIndex：endIndex】，从beginIndex开始，到索引endIndex结束（不包含endIdnex）
'''
sub_str = define_str[1:3]
# print sub_str  #输出汉语貌似有问题
'''
define_eng_str = "I love Python"
sub_str = define_eng_str[2:6]
print sub_str
print define_eng_str[-11:-7]
print define_eng_str[2]   #只输出一个：l
print define_eng_str[2:]  #输出love Python