"""
将一个骰子掷6000次，统计每一面出现的次数
 
运用列表，将 1 存在 fs[0]中，2 存在 fs[1]中，依次类推。。。
"""

import random

# 列表的重复运算
fs = [0] * 6  # fs = [0, 0, 0, 0, 0, 0]

for _ in range(6000):
    face = random.randrange(1, 7)
    fs[face - 1] += 1
for i, x in enumerate(fs):
    print(f'{i+1}点有： {x}次')