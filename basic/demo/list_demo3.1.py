"""
向列表中随机添加10个数，找到其中第二大的数

理解算法思想，注意16行
"""

nums = [23, 31, 42, 12, 23, 67, 53, 75, 75]

# m1是最大值，假定为nums[0]； m2是第二大值，假定为nums[1]
m1, m2 = nums[0], nums[1]
if m1 < m2:
    m1, m2 = m2, m1
for i in range(2, len(nums)):
    if nums[i] > m1:
        m1, m2 = nums[i], m1
    elif nums[i] == m1:  # 当出现两个最大值的时候， 跳出本次循环。判断位置一定要在第三个判断之前。
        pass
    elif nums[i] > m2:
        m2 = nums[i]

print(m1, m2)