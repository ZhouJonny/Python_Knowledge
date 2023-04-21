"""
如何一次取得一个字典中多个指定的值？
"""

data_dict = {'a': 1, 'b': 2, 'c': 3}

# 取出单个的值
print('[取出单个的值]', data_dict.get('a'))

# ERROR 只输出1
print(data_dict.get('a', 'b'))


keys = ['a', 'c']  # 指定要取出的值
values = []  # 得到的值

# 1.for循环遍历
for k, v in data_dict.items():
    if k in keys:
        values.append(v)
    continue
print('[for循环遍历]', values)

# 2.推导式***
values = [data_dict.get(key) for key in keys]
print('[推导式]', values)

# 3.高阶函数
"""
map(function, iterable) 
函数将一个函数 function 应用于一个可迭代对象 iterable 中的每个元素，并返回一个可迭代的结果。
"""
values = list(map(data_dict.get, keys))
print('[高阶函数]', values)


"""
map()
"""
# 1.将一个列表中的每个元素转换为字符串类型
numbers = [1, 2, 3, 4, 5]
strings = list(map(str, numbers))
print(strings)