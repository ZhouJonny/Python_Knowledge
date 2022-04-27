"""
在设计函数的时候，函数的参数个数是暂时无法确定的
    * 可变参数（元组）
        *args ---> 可变参数（在变量名前加*）---> 可以接收0个或任意多个位置参数 ---> 将所有的位置参数打包成元组
    * 关键字参数（字典）
        **kwargs --->可以接收0个或任意多个位置参数 ---> 将所有的关键字参数打包成字典
"""


def add(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))
    # return sum(int(args))  # 如果args里有string，则会有bug
    total = 0
    for arg in args:
        if type(arg) in (int, float):  # arg为整数或者小数
            total += arg
    for value in kwargs.values():
        if type(value) in (int, float):
            total += value
    return total


print(add(1, '2', 3, a=1, b=3, c=5, d='hello'))
