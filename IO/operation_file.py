# coding=utf-8

"""
使用python命令操作文件
"""
import os

print "操作系统的名字：%s" % os.name  # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print "详细信息:", (os.uname())
print "环境变量：", os.environ
print "获取用户名:",os.getenv('USER')

# 操作文件和目录
"""
操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
"""
print "当前目录：",os.path.abspath('.')
# 添加目录
join_path = os.path.join(os.path.abspath('.'), 'pythonCreate')  # 创建路径
# print os.mkdir(join_path)   # 生成目录
# print os.rmdir(join_path)  # 移除目录