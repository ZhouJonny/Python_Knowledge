'''
列表中元素为字符串时，要将其转换成int
'''
nums = ['1', '10', '234', '2', '35', '100']
nums.sort()
print(nums)  # 输出字符串比较大小的结果
nums2 = [int(num) for num in nums]  # 用生成式将nums中的元素变成int型
nums2.sort()
print(nums2)
# 以上方法不推荐，用sort()中的key
nums.sort(key=int)
print(nums)