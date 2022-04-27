"""
字典的创建和使用
"""
# 空字典
student_dict = {}
# 空集合
student_set = set()

# 字面量语法
student1 = {
    'name': 'jonny',
    'sex': True,
    'id': '2015123221',
    'city': 'Shanghai',
}
print(student1.values())
print(len(student1))
# 对所有的键进行遍历 ---> student1/student1.keys(), 可以用过下标运算获取值
for key in student1:
    print(key, student1[key])
print('-' * 20)
# 对所有的值进行遍历 ---> student1.values()
for value in student1.values():
    print(value)
print('-' * 20)
# 对键值进行遍历 ---> student1.items()
for key, value in student1.items():
    print(key, value)

# 构造器函数
student2 = dict(name='zyj', sex=True)

# 生成式语法
# * 列表
list1 = [i for i in range(1, 10)]
print(list1)
# * 集合
set1 = {i for i in range(1, 10)}
print(set1)
# *字典
dict1 = {i: i ** 2 for i in range(1, 10)}
print(dict1)