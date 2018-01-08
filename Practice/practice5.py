# 可变参数
# 使用*开头，有点儿类似于解析赋值，只不过实参和形参表现不同，形参表示该参数是可变的

# 求任意个数的数字的平方和
def squareSum(*nums):
    print(nums)
    print(type(nums))  # <class 'tuple'>
    sum = 0
    for num in nums:
        sum = sum + num ** 2
    return sum

result1 = squareSum(1,2,3)
print(result1)

result2 = squareSum(*(1, 2, 3))  # 如果不带*，则nums为((1, 2, 3),)
print(result2)

result3 = squareSum(*[1, 2, 3])  # 如果不带*，则nums为([1, 2, 3],)
print(result3)
