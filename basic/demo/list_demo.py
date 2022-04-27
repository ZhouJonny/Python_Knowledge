"""
向列表中随机添加10个数，找到其中第二大的数
"""
import random

nums = [random.randrange(20, 101) for _ in range(10)]
print(nums)
nums.remove(max(nums))
print(max(nums))