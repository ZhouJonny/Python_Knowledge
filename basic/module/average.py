import random


def average_func(nums):
    sum = 0
    for num in nums:
        sum += num
    return sum / len(nums)


# __name__是一个隐藏变量，它代表当前模块（文件）的名字
# 如果直接通过python解释器运行average.py，__name__的值是__main__ ---> if __name__ == '__main__': 的内容会被执行
# 如果在其他模块 （文件）中导入average.py，此时__name__的值是average.py ---> if __name__ == '__main__': 的内容不会被执行
if __name__ == '__main__':
    nums = [random.randrange(1, 100) for _ in range(10)]
    print(nums)
    print(f'这是在average.py中的：{average_func(nums)}')