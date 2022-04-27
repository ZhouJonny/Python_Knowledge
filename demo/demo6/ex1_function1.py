'''
函数的参数1
函数：相对独立，且会被重复使用的功能。将来咋再想使用这些功能的时候，不是去复制代码，而是直接通过函数调用。
python不需要重载，定义一个函数的时候可以让它有不同的使用方式
'''
from random import randint

def fun1(n=2):
    '''摇骰子，默认两次机会'''
    total = 0
    for _ in range(2):
        total += randint(1,6)
    return total

print(fun1())  # 如果没有指定参数那么使用默认值摇骰子
print(fun1(4))  # 摇四颗骰子
