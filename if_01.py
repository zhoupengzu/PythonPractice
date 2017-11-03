# coding=utf-8
a = 10
if a < 60:
    print "不及格"
elif a >= 60 and a < 90:      #python没有&&的逻辑运算符，单个&表示位与
    print "良好"
else:
    print "优秀"