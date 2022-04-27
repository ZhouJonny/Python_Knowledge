"""
双色球随机选号
"""
import random


def generate():
    """
    生成一组彩票号码

    :return: 保存一组彩票号码的列表
    """
    red_balls = [i for i in range(1, 34)]
    blue_balls = [i for i in range(1, 17)]
    select_reds = random.sample(red_balls, 6)
    select_reds.sort()
    select_balls = select_reds + random.sample(blue_balls, 1)
    return select_balls


def display(balls):
    """
    显示一组彩票号码

    :param balls: 装彩票号码对应的球列表
    :return:
    """
    for ball in balls:
        print(f'{ball:*>5d}', end='')
    print()


n = int(input('机选几注：'))
for _ in range(n):
    # 类似复合函数 y = g(f(x))
    display(generate())