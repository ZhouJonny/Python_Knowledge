"""
字典相关操作
"""
dict1 = {'A': 100, 'B': 200, 'C': 300}
dict2 = {'E': 400, 'F': 500, 'A': 600}

# 更新(元素的更新或合并) ---> update()
"""
* 字典不可以 dict1 + dict2
* dict2里的内容更新到dict1中，以dict2为主
"""
dict1.update(dict2)
print(dict1, len(dict1))

# 删除 ---> 键必须存在，如果不存在会产生KeyError ---> del/pop()/popitem()
del dict1['A']  # 删除，不会反对值
dict1.pop('B')  # 删除，会返回值
dict1.popitem()  # 删除字典里最后一个键值对
print(dict1, len(dict1))

# 清空
dict1.clear()
print(dict1)