"""
- 幸运的女人 （Josephu环）
有15个男人和15个女人坐船出海，船坏了，需要把其中15个人扔到海里，其他人才能活下来；
所有人国成一圈，由某个人从1开始依次报数，报到9的人被扔到海里，下一个人重新从1开始报数，
直到将15个人扔到海里。最后。15个女人都幸存了下来，15个男人都被扔到了海里，
问原先哪些位置是男人，哪些位置是女人
"""
persons = [True] * 30
# 30人编号， 计数器大于15时终止循环， 报数 9扔下去
index, counter, number = 0, 0, 0
while counter < 15:
    if persons[index]:  # 值为True才进入此分支，即没被扔下去的人
        number += 1  # 没被扔下去的人开始报数
        if number == 9:
            persons[index] = False  # 扔下去
            counter += 1  # 计数器加一
            number = 0  # 从头开始报数
    index += 1
    # 防止列表索引越界
    if index == 30:
        index = 0

for person in persons:
    if person:
        print('女', end='')
    else:
        print('男', end='')
print('#'*20)
# 等价于以下三元条件运算 ---> if 后面的表达是为True，就取if前面的值，否则取else后面的值
for i in persons:
    print("女" if i else "男", end='')

# 另一种方法：
people = [i for i in range(1, 31)]
for _ in range(15):
    people = people[9:] + people[:8]
for j in range(1, 31):
    print("女" if i in people else '男')