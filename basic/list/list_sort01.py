"""
简单选择排序：每趟排序都从未被确定位序部位中选择最小的元素
"""
nums = [35, 12, 99, 58, 67, 42, 49, 31, 73]
# 前 i-1个元素都是已经排好序的元素，默认i是未排序中最小的元素，通过内循环找到未排序中真正最小的元素，与i进行交换
for i in range(0, len(nums)-1):
    # 假设第一个元素就是最小的元素
    min_value, min_index = nums[i], i
    # 内循环从未排序元素中找到最小的那个，与 i 进行交换
    for j in range(i+1, len(nums)):
        if nums[j] < min_value:
            min_value, min_index = nums[j], j
    # 交换，让i变成最小的元素
    nums[i], nums[min_index] = nums[min_index], nums[i]
print(nums)