"""
元祖(tuple) ---> 不可变容器
创建一个元祖比创建一个列表的时间、空间开销更小
元祖只能进行读操作， 写操作都做不了

* 重复运算
* 成员运算
* 合并运算
* 索引
* 切片
* index()
* count()
"""
fruit = ('apple', )  # 一元祖一定要加 ,  否则就会被认为是字符串加了括号被提升优先级
print(type(fruit))
fruits1 = ('apple', 'banana', 'grape')
# 重复运算
print(fruits1 * 3)
# 成员运算
print('apple' in fruits1)
print('grape' not in fruits1)
# 合并运算
fruits2 = ('pitaya', 'litchi')
fruits3 = fruits2 + fruits1  # 不改变原来的元祖， 生成一个新元祖
print(fruits3)
# 索引
print(fruits3[4], fruits3[-1])
# 切片
print(fruits3[1:4])  # 输出第二个 第三个 第四个
print(fruits3[1:4:2])  # 输出第二个 第四个 步长为2
print(fruits3[::-1])  # 反转
# index() ---> 返回索引下标
print(fruits3.index('apple'))
# count() ---> 返回出现次数
print(fruits3.count('apple'))