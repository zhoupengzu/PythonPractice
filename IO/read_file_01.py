# coding=utf-8

status = 0
"""
两种读取文件内容的方式(这里是一次性读取)
"""
if status == 0:
    try:
        local_file = open('./麦芽分期.rtf', 'r')
        print local_file.read()
    except IOError, e:
        print e
    finally:
        if local_file:
            local_file.close()
else:
    with open('./麦芽分期.rtf', 'r') as local_file:
        print local_file.read()
