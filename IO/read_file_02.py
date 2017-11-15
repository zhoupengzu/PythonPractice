# coding=utf-8

"""
复习
"""
path = './麦芽分期.rtf'
# # 方式一
# try:
#     local_file = open(path,'r')
#     print local_file.read()
# except IOError, e:
#     print e
# finally:
#     if local_file:
#         local_file.close()
#
# # 方式二
# with open(path,'r') as local_file:
#     print local_file.read()
#

"""
调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。
因此，要根据需要决定怎么调用
"""
with open(path,'r') as local_file:
    print local_file.read(128)

with open(path, 'r') as local_file:
    print local_file.readline(4)

with open(path, 'r') as local_file:
    print local_file.readlines(1)
