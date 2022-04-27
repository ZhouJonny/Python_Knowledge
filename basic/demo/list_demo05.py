"""
用一个列表保存54张扑克牌，先洗牌，
再按斗地主的发牌方式把牌发给三个玩家，多的3张牌给第一个玩家（地主），
最后把每个玩家手上的牌显示出来
"""
import random

suites = ['♠️', '♥️', '♣️', '♦️']
faces = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# cards = []
# for suite in suites:
#     for face in faces:
#         cards.append(f"{suite}{face}")
# 用列表生成式语法简化上述代码
cards = [f'{suite}{face}' for suite in suites for face in faces]
cards.append("大王")
cards.append("小王")
# 洗牌
random.shuffle(cards)

# 定义三个玩家，玩家1是地主
player_one = []
player_two = []
player_three = []
# 发牌，每人17张，地主再拿3张
for _ in range(17):
    player_one.append(cards.pop())
    player_two.append(cards.pop())
    player_three.append(cards.pop())
player_one.extend(cards)  # cards最后还剩三张牌 ，都给地主

# 按牌的点数排序（忽略花色）
player_one.sort(key=lambda x: x[2:])
player_two.sort(key=lambda x: x[2:])
player_three.sort(key=lambda x: x[2:])

print(player_one)
print(player_two)
print(player_three)