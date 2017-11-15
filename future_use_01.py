# coding=utf-8
'''
打开不打开下面的这一行，可以看到输出结果不同，因为在python2 中如果是整数之间的相除，会做地板除法，即省略小数，但是在python3中是精确除法
'''

# from __future__ import division

print '10 / 3 = ',10 / 3
print '10.0 / 3 = ' , 10.0 / 3
print '10 // 3 = ', 10 // 3