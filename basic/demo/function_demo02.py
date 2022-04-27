"""
双色球或大乐透随机选号
    代码重构 ---> 将重复的部分抽取出来成方法
"""
import random


def generate(ball_max, ball_num):
    """
    选择一组随机的球

    :param ball_max: 球的最大值
    :param ball_num: 选择几个球
    :return:
    """
    balls = [i for i in range(1, ball_max + 1)]
    selected = random.sample(balls, ball_num)
    selected.sort()  # 对球的值进行排序
    return selected


def display(balls):
    for ball in balls:
        print(f'{ball:0>2d}', end=' ')
    print()


def make_big_lottery():
    return generate(35, 5) + generate(12, 2)


def make_two_colors():
    return generate(33, 6) + generate(16, 1)


n = int(input('机选几注：'))
print('大乐透：')
for _ in range(n):
    display(make_big_lottery())
print('双色球：')
for _ in range(n):
    display(make_two_colors())