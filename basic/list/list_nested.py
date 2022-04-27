"""
用一个列表保存54张扑克牌，先洗牌，
再按斗地主的发牌方式把牌发给三个玩家，多的3张牌给第一个玩家（地主），
最后把每个玩家手上的牌显示出来

# 本段代码是对list_demo05使用嵌套列表后的优化

* 嵌套列表的生成式语法 players = [[] for _ in range(3)]
* append() ---> 追加元素（添加到末尾）
* random.shuffle() ---> 对列表本身进行打乱
* pop() ---> 删除元素（默认删除最后一个元素）
* sort() ---> 对列表的元素进行排序（列表的元素为字符串时，用 key = int 进行转换）
"""
import random

suites = ['♠️', '♥️', '♣️', '♦️']
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# 两个for循环的列表生成式语法
cards = [f'{suite}{face}' for suite in suites for face in faces]
cards.append('小王')
cards.append('大王')
random.shuffle(cards)

# 创建玩家并分牌
# player_one = []
# player_two = []
# player_three = []
# 对以上代码优化
# player = [[]] * 3  # 错误！！！会生成三个一样列表，内存地址一样
players = [[] for _ in range(3)]  # 使用嵌套列表（列表中又是列表）

# for _ in range(17):
#     player_one.append(cards.pop())
#     player_two.append(cards.pop())
#     player_three.append(cards.pop())
for _ in range(17):
    for player in players:
        player.append(cards.pop())

# player_one.extend(cards)
players[0].extend(cards)

# print(player_one)
# print(player_two)
# print(player_three)
for player in players:  # 对玩家进行循环
    player.sort(key=lambda x: x[2:])
    for card in player:  # 对每个玩家
        print(card, end='')
    print()