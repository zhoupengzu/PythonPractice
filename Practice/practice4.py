# 关键参数

def add(num1, num2):
    result = num1 + num2
    return result

# 正常调用
result1 = add(2, 3)
# 关键参数调用
result2 = add(num2 = 4, num1 = 5)
print(result2) # 9
