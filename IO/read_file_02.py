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
