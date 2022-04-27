import random

names = ['name1', 'name2', 'name3', 'name4', 'name5', 'name6']

print(len(names))
# sample() ---> 对列表元素进行无放回抽样
print(random.sample(names, k=3))
# choices ---> 对列表元素进行有放回抽样（可以重复抽中）
print(random.choices(names, k=3))
# choice ---> 可以从列表中随机选择一个元素
print(random.choice(names))
# shuffle() ---> 实现对列表元素进行原地打乱
random.shuffle(names)
print(names)