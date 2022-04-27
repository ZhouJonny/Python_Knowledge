"""
有一个放整数的列表，找出列表中出现次数最多的元素
"""
nums = [2, 2, 5, 64, 3, 9, 5, 64, 9, 2, 9]

# 默认第一个是出现次数最多的元素
# 将items设置成列表，可能有多个出现次数最多的元素
items, max_count = [nums[0]], nums.count(nums[0])
# nums[1:] ---> 从nums的第二个元素开始遍历
for num in nums[1:]:
    cur_count = nums.count(num)
    if cur_count > max_count:
        items.clear()
        max_count = cur_count
        items.append(num)
    elif cur_count == max_count:
        if num not in items:  # 去重, 否则会把所有最多出现次数的元素都放进去
            items.append(num)

print(items, max_count)