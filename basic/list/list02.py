"""
列表相关操作

* 列表的生成 ---> 字面量，构造器，生成式
* 遍历列表的元素 ---> 三种方法，*enumerate() 枚举函数
* 列表相关运算
    @ 成员运算
    @ 重复运算
    @ 索引和切片
    @ 合并
        list1 + list2
        list1.extend(list2)
* 列表的反转
    @ list[::-1]
    @ list.reverse()
* 列表的排序
    @ list.sort()  # 默认升序
    @ list.sort(reserve=True)  # 使用关键字，变成降序
"""
# 列表的生成
# 字面量语法生成列表
list1 = ['apple', 'orange', 'banana']
print(list1)
# 构造器语法生成列表
list2 = list(range(1, 10))
print(list2)
# 推导式（生成式）语法构造列表
list3 = [i ** 2 for i in range(1, 10, 2)]
print(list3)

# 获取列表元素的个数 ---> len()
print(len(list3))

# 遍历列表中的元素
for i in range(len(list1)):
    print(list1[i])
for x in list1:
    print(x)
for i, x in enumerate(list1):
    print(i, x)

# 和列表相关的运算
# 重复运算
list4 = [1, 2, 3, 4] * 4
print(list4)
# 成员运算 ---> Ture/False
print(10 in list4)
print(2 in list4)
print(20 not in list4)
# 索引和切片
# 正向索引： 0 ～ N-1/ 负向索引： -N ～ -1

# 合并
list5 = [1, 3, 5, 7]
list6 = [4, 4, 8]
print(list6 + list5)
# 合并 ---> extend()
list6.extend(list5)
print(list6)

# 比较
# 数字和字符串无法比大小
list7 = list(range(1, 8, 2))
list8 = [0, 1, 3, 5, 7, 9]
print(list5 == list7)
print(list8 == list7)
# 比较两个列表对应位置元素的大小
print(list7 < list8)

# 列表的反转
items = ['banana', 'grape', 'apple', 'waxberry', 'pitaya', 'apple']
print(items[::-1])  # 并不是对items进行反转
print(items)  # 输出的还是items
items.reverse()  # 对items进行反转
print(items)

# 列表的排序
items.sort()  # 默认升序
items.sort(reverse=True)  # 可以通过reverse参数控制升序或者降序
