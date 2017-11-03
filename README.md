# PythonPractice
**************************Python2**************************
一、基础
1、编码
在python2中不允许有中文，如果有中文，需要在文件开头添加一句：# coding=utf-8

2、定义
标识符（变量？）可以包括字母、数字和下划线，但是不能以数字开头；
但是以下划线开头的有特殊意义：
 1）单下划线开头代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
 2）双下划线开头代表私有成员
 3）以双下划线开头和结尾的代表 Python 里特殊方法专用的标识，如 __init__() 代表类的构造函数
 
 3、行和缩进
 1）代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块
 2）缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。下述的例子将会报错
 if True:
    print "True"
else:
  print "False"
  
 4、多行语句
 用\来定义多行，如：
 total = item_one + \
        item_two + \
        item_three
 
 
 5、引号
 可以使用单引号、多引号、三引号（'''或者"""），其中三引号可以由多行组成，如：
 paragraph = """这是一个段落。
包含了多个语句"""

6、注释
单行注释使用#号就好，多行注释使用三引号

7、输出
print，如果在print后添加"，"号则不换行输出，否则换行输出

