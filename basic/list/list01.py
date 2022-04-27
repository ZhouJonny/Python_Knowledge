"""
列表的遍历（把每个元素依次取出来）

索引运算 - 通过正向或负向索引获取元素

* len() --> length: 给出列表中有多少个元素
* append() ---> 追加元素，在列表末尾添加元素
* insert() ---> 插入元素，在指定位置插入元素
* pop() ---> 删除并返回最后一个元素
* del num[i] ---> 删除指定位序i的元素
* remove(x) ---> 删除指定元素值为x的元素
* clear() ---> 清空列表
* index(x) ---> 若x在列表中，则返回位序，否则程序会崩溃。所以要加if判断
* count(x) ---> 统计元素x在列表中出现几次
* enumerate() ---> 枚举函数
"""

# 创建列表的自变量语法
nums = [22, 341, 52, 345]

# 列表的索引
# 输出第一个元素
print(nums[0], nums[-4])
# 输出第三个元素
print(nums[2], nums[-2])
# 输出最后一个元素
print(nums[3], nums[-1])

# 将第三个元素的值改为120
nums[2] = 120
print(nums)

# 追加元素（把元素放到列表的末尾）
nums.append(1000)
# 插入元素（在指定位置插入元素）
nums.insert(0, 1)

# 删除元素（默认删除最后一个）
nums.pop()
# 删除元素（指定元素位置）
del nums[1]
# 删除值为345的元素
nums.remove(345)
# 删除列表中所有值为22的值
while 22 in nums:
    nums.remove(22)
# 清空列表
nums.clear()

# index() ---> 若元素在列表中，则返回位序。不在则程序崩溃
items = ['apple', 'banana', 'grape', 'waxberry', 'pitaya', 'apple']
# caomei 不在items中，执行会报错。所以通常写if!!否则程序会崩溃
if 'caomei' in items:
    print(items.index('caomei'))  # 这段代码不会执行
# 返回第一个apple在列表中的位置
if 'apple' in items:
    print(items.index('apple'))
# 从3开始，返回apple在列表中的位置
if 'apple' in items:
    print(items.index('apple', 3))
# count() ---> 统计这个元素在列表中出现了几次
print(items.count('apple'))

# 列表的遍历
# 法一：既可以做读操作，也可以做写操作
for i in range(len(nums)):  # 用len()函数得出列表的长度
    print(nums[i])
    # nums[i] = 100  # 列表里的每个元素都变成100
print('-'*20)
# 法二：只读循环
for num in nums:  # for循环不但可以放range， 还可以放容器
    print(num)
print('*'*20)
# 法二.1 enumerate() --> 枚举函数，生成两个值，第一个是位序，第二个是列表元素(!!推荐)
for i, x in enumerate(nums):
    print(i, x)