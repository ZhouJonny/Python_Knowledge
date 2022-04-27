"""
一个列表中有很多重复的元素，写一段代码去掉列表中重复的元素
"""

nums = [2, 2, 5, 64, 3, 9, 5, 64, 9]
nums1 = []
for x in nums:
    if x in nums1:
        pass
    else:
        nums1.append(x)
print(nums1)