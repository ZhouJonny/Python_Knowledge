"""
函数的作用 ---> 去掉重复的代码，将相对独立且会被重复使用的功能（代码）整合起来，将来想使用这些功能的时候，不需要再复制粘贴代码，而是通过调用函数来做到

def f(x):  # 传入自变量x ---> 参数（parameter）---> 多个参数用, 隔开

    return y  # 返回因变量y ---> 返回值（return value）
* ！！设计函数最重要的事情：一个函数只做做好一件事情
"""
import random


def roll_dice(num=2):  # 如果调用函数的时候，没有给参数，就调用默认值
    """
    摇骰子

    :param num: 骰子的数量（对自变量的说明）
    :return: 骰子的点数（对因变量的说明）
    """
    total = 0
    for _ in range(num):
        total += random.randrange(1, 7)
    return total


first_point = roll_dice(3)  # 使用参数3
second_point = roll_dice()  # 使用默认值2
print(first_point, second_point)