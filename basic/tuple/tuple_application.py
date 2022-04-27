# ValueError: too many values to unpack
# 执行报错，三个变量 五个值
a, b, c = 5, 10, 15, 20, 25
print(a)
print(b)
print(c)

# a=5 c=25 b=[10,15,20]
a, *b, c = 5, 10, 15, 20, 25
print(a)
print(b)
print(c)

# a=5 b=10 c=[15,20,25]
a, b, *c = 5, 10, 15, 20, 25
print(a)
print(b)
print(c)

# a=[5,10,15] b=20 c=25
*a, b, c = 5, 10, 15, 20, 25
print(a)
print(b)
print(c)

# 只想取头和尾, 中间元素 用 _ 表示
a, *_, c = 5, 10, 15, 20, 25
print(a)
print(c)