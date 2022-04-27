"""
向列表中随机添加10个数，找到其中第二大的数

1. for循环在外创建列表的两种写法
2. for循环在内的推导式写法
3. remove()
4. pop()
"""
import random

nums = []
# 写法1：for循环在外面
for _ in range(10):
    # random()生成[0,1)之间的小数
    # 写法1.1:
    temp = random.random() * 100
    nums.append(temp)
    # 写法1.2：
    nums.append(random.random() * 100)
# 写法2：把for循环放到列表中(推导式) ==> 高级写法！！执行速度会更快，创建列表的时候，推荐使用这样的语法
nums = [random.random() * 100 for _ in range(10)]
# 写法2.1 创建1-100的奇数(推导式)
nums = [i for i in range(1, 101, 2)]
print(nums)

max_value = max(nums)
print(max_value)
# pop(i) ---> 删除位序为i的元素
# remove(x) ---> 删除值为x的元素
nums.remove(max_value)
print(max(nums))