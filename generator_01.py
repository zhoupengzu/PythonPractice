# coding=utf-8
#生成器：根据某种规则可以推算出需要的结果，这样就可以避免list生成器所造成的空间浪费
#生成器和list生成式的区别在于：将list生成式的中括号改成小括号，可以通过next方法访问，也可以通过for循环访问
generator = (n*n for n in range(1,5))
print generator #<generator object <genexpr> at 0x1001aca50>
print generator.next()  #1

for value in generator:
    print value
