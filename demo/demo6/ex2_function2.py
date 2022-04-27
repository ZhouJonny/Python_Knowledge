'''
函数的参数2
ex1的函数设定了默认值，所以在函数调用的时候如果没有传入对应的参数，就使用对应参数的默认值
'''
# 对于add函数，可以使用不同的方式去调用add函数
def add(a=0, b=0, c=0):
    return a+b+c
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(c=2, a=1, b=4))  # 传递参数的时候可以不按照设定的顺序进行传递

# 当对多个参数进行加法运算的时候，具体的参数是由调用者决定的，在不确定参数个数的时候，可以用可变参数。
# 在参数名前加*，表示args是一个可变参数
def add1(*args):
    total = 0
    for _ in range(args):
        total += args
    return total
# 在调用add1函数时，可以传递一个或多个参数
print(add1())
print(add1(1))
print(add1(1,3,5))
print(add1(2,4,6))
