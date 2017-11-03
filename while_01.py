# coding=utf-8
i = sum = 0
while i <= 100:
    sum += i
    i += 1
print "sum=",sum

count = 100
odd_list = []  #奇数
even_list = [] #偶数
while count >= 0:
    if count % 2 == 0:
        even_list.append(count)
    else:
        odd_list.append(count)
    if count <= 50:
        break     #如果break了，则不会执行else
    count -= 1
else:
    print odd_list

print even_list