"""
冒泡排序： 元素两两比较，如果后面的元素小于前面的元素，就交换两个元素的位置
"""
nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]
lists = [9, 1, 2, 3, 4, 5, 6, 7, 8]  # 算法要针对这种情况进行优化

# 每次循环，最小的都会"沉底"
for i in range(len(nums)-1, 0, -1):
    swapped = False  # 优化算法，swapped值默认为false。只有进行内循环，即
    for j in range(0, i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
            swapped = True
        if not swapped:
            break  # 没有执行内循环。直接break。
print(nums)