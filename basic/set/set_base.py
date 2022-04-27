"""
集合的定义
* 无序性 ---> 不能使用下标索引
* 互异性 ---> 不能有重复的元素
"""
# 字面量语法创建集合
set1 = {1, 2, 4, 6, 1, 2}
print(type(set1))
# 互异性（没有重复元素）
print(set1, len(set1))
# 无序性
# TypeError: 'set' object is not subscriptable
# print(set1[0])

# 遍历集合中的元素
for elem in set1:
    print(elem)

# 这不是空集合，而是字典
set2 = {}
print(type(set2))

# 只能用构造器语法创建空集合
set3 = set()
print(type(set3))