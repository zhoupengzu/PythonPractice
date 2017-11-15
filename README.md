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

二、数据类型
有数字（Number）、字符串（String）、列表（List）、元祖（Tuple）、字典（Dictionary）

1、定义变量
定义变量不需要指出类型，赋值的时候也不需要，见type_01s

2、数字Number，见type_02
支持int、long、float和complex（复数）

3、字符串String，见type_03

4、列表(即数组)，见type_04

5、元祖，见type_05
和列表类似，但是不能更新内容，即只读的

6、字典，见type_06

三、运算符
除了常用的，这里只收录不常见的
1、算数运算符，见operator_01
a = 10,b = 20
1)a**b:表示a的b次幂
则表示10的20次方
2）//：取整除

2、逻辑运算符
and、or、not

3、成员运算符，见operator_02
in、not in
用于查找字符串、列表和元祖中是否存在某个对象

4、身份运算符，见operator_03
is、is not
用于判断两个对象是否引用同一个对象

四、条件语句，见if_01

python没有switch语句

if a:
    ...
else:
    ...
    
或者
if a:
    ...
elif:
    ...
elif:
    ...
else:
    ...
    
五、循环语句（while和for）
1、while，见while_01

2、for，见for_01
for循环可以遍历任何序列的项目，如一个列表或者一个字符串

六、pass语句
是空语句，是为了保持程序结构的完整性。
pass 不做任何事情，一般用做占位语句，例如：
# 输出 Python 的每个字母
for letter in 'Python':
   if letter == 'h':
      pass
      print '这是 pass 块'
   print '当前字母 :', letter

print "Good bye!"

输出：
当前字母 : P
当前字母 : y
当前字母 : t
这是 pass 块
当前字母 : h
当前字母 : o
当前字母 : n
Good bye!

七、函数，见function_01
1、定义
用def定义一个函数，格式为：
def functionName():
    ...

2、传参
不可变类型：类似 c++ 的值传递，如 整数、字符串、元组。如fun（a），传递的只是a的值，没有影响a对象本身。比如在 fun（a）内部修改 a 的值，只是修改另一个复制的对象，不会影响 a 本身。
可变类型：类似 c++ 的引用传递，如 列表，字典。如 fun（la），则是将 la 真正的传过去，修改后fun外部的la也会受影响
参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值
参数允许设置默认值

八、别名
import 模块名 as 别名
如：import cStringIO as StringIO 表示将cStringIO导入并起别名StringIO
如果导入失败，会报错误，可以捕获这种错误
try:
    import cStringIO as StringIO
except ImportError: # 导入失败会捕获到ImportError
    import StringIO