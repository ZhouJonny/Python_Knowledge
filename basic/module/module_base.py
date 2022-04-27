"""
模块
* 如果想要使用其他文件（模块）中定义的函数，可以使用import导入模块，然后通过模块名.函数名()的方式调用函数
* 还可以从模块中直接导入函数 ---> from 模块 import 函数 ---> 就可以直接通过函数名()调用函数了
    此方法还可以使用as 进行别名
"""
import random
# import average
from average import average_func
# from average import average_func as avg  ---> 使用avg别名来调用average_func

nums = [random.randrange(50, 100) for _ in range(10)]
print(nums)
# print(f"{average.average(nums)}")  # if __name__ == '__main__'的内容不会被执行
print(f'{average_func(nums)}')