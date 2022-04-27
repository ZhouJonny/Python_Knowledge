"""
字符串（string ）
注意：
    字符串也是不变数据类型，只能进行读操作，不能进行改写操作

* 原始字符串 r
* 格式化字符串 f
* ord() ---> 查看字符编码值
* 重复运算 ---> a * 5
* 成员运算 ---> 'hello' in a
* 字符串拼接 ---> a + b
* 比较运算 ---> 比较字符串内容是否一样
* 遍历字符串 ---> 同遍历列表
"""
a = 'hello, world'
b = "hello, world"
c = ''' 
line1
line2
line3
'''  # 这种字符串中间可以折行
print(a)
print(b)
print(c)

# 字符串改写错误
# TypeError: 'str' object does not support item assignment
# a[0] = 'H'

# 原始字符串，每个字符串都是原始的含义，不进行转译
d = r'c:\Users\Admin'
print(d)

# 格式化字符串
e = f'文件路径:{d}'
print(e)

# 重复运算
print(a * 5)

# 成员运算
print('lo' in a)
print('ko' in a)

# 字符串拼接
print(a + b)

# 比较运算，比较字符串的内容是否一样 ---> 字符串编码大小 ord()
print(a == b)
print(a != b)

# 遍历字符串
for i in range(len(a)):
    print(a[i])
for i in a:
    print(i)