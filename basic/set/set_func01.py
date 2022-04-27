"""
集合的运算
"""
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}

# 成员运算 - 确定性（元素要么在集合中，要么不在集合中）
# 集合的成员运算在效率上远远高于列表的成员运算
print(1 in set1)
print(1 not in set1)

# 交集
print(set1 & set2)
print(set1.intersection(set2))

# 并集
print(set1 | set2)
print(set1.union(set2))

# 差集
print(set1 - set2)
print(set1.difference(set2))
print(set2 - set1)

# 对称差
print(set1 ^ set2)
print((set1 | set2) - (set1 & set2))
print(set1.symmetric_difference(set2))

set3 = {1, 2, 3, 4, 5, 6, 7, 8, 9}
# 判断真子集
print(set1 < set3)
# 判断子集
print(set1 <= set3)
# 判断超集
print(set3 > set1)