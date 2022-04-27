"""
对一床扑克牌洗牌、发牌
"""
import random

from poker01 import Card
from poker01 import Suite


class Poker:
    def __init__(self):  # 数据抽象
        # self.cards = []
        # for suite in "SHCD":
        #     for face in range(1, 14):
        #         """
        #         !!! 如果没有poker01.py里的__str__或者__repr__这两个魔术方法，card的结果则是Card()在内存中的地址。
        #         """
        #         card = Card(suite, face)
        #         self.cards.append(card)

        # self.cards = [Card(suite, face) for suite in 'SHCD' for face in range(1, 14)]
        self.cards = [Card(suite, face) for suite in Suite for face in range(1, 14)]
        self.counter = 0

    def shuffle(self):
        """洗牌"""
        self.counter = 0  # 每次发牌counter都从0开始
        random.shuffle(self.cards)

    def deal(self):
        """发牌

        每次发出一张牌
        """
        card = self.cards[self.counter]
        self.counter += 1
        return card

    def has_more(self):
        """是否还有牌"""
        return self.counter < len(self.cards)


def main():
    poker = Poker()
    # print(poker.cards)  ---> 生成的有序扑克牌列表
    poker.shuffle()
    # print(poker.cards)
    while poker.has_more():
        print(poker.deal())


if __name__ == '__main__':
    main()