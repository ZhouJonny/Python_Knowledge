"""
字符串的操作 - 在字符串中查找有没有某个子串，若找到则返回相对应的位置

* index / rindex
* find / rfind ---> 推荐使用
"""

a = "Oh apple, i love apple."
# index() ---> 从左往右找第一个出现的位置，可以指定从哪开始找，默认是0
# 找到了返回子串对应的索引，找不到直接报错（程序崩溃）
print(a.index('apple'))
print(a.index('apple', 10))
# rindex() ---> 从右往左数第一个出现的位置
print(a.rindex('apple'))

# find() 与 index() 作用相同，但是find() 找不到不会引起程序崩溃，会返回-1
print(a.find('apple'))
print(a.find('apple', 100))
print(a.rfind('apple'))