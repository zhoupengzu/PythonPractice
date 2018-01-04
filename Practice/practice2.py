# range(a, b， step)，其中a代表起始数字，b代表结束数字，区间是左闭右开的，step代表步长，大于0则增加，小于0则减小,且该参数不能为0
for x in range(10, 20):
    print(x, end='|')
else:
    print()
print('带有步长的：')
for x in range(20, 30, 2):
    print(x, end='|')
else:
    print()

for x in range(30, 20, -2):
    print(x, end='|')
else:
    print()

for x in range(30, 20, 0):
    print(x, end='|')
else:
    print()