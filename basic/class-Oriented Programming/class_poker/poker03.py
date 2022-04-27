"""
玩家进行抓牌
"""
from poker02 import Poker


class Player:

    def __init__(self, nickname):
        self.nickname = nickname  # 每个玩家都有昵称，self的nickname就是传进去的nickname
        self.cards = []  # 每个玩家都有牌

    def get_one_card(self, card):
        """摸一张牌"""
        self.cards.append(card)

    def arrange(self):
        """玩家给手中的牌排序"""
        """
        注意poker01.py里的__lt__
        """
        self.cards.sort()

    def show(self):
        """显示玩家手中的牌"""
        print(self.nickname, end=":")
        for card in self.cards:
            print(card, end=' ')
        print()  # 换行
        print(f'{self.nickname}共{len(self.cards)}张牌')


def main():
    print("main")
    player1 = Player('Jonny')  # 创建玩家对象
    player2 = Player('zyj')
    poker = Poker()  # 创建扑克对象
    poker.shuffle()  # 洗牌
    for _ in range(15):
        card = poker.deal()  # 发一张牌
        player1.get_one_card(card)
        card = poker.deal()  # 再发一张牌
        player2.get_one_card(card)
    player1.show()
    player2.show()
    print('-'*20)


def main_pro():
    """
    创建四个玩家，每个玩家发13张牌

    :return:
    """
    print('mian_pro')
    poker = Poker()  # 创建扑克对象
    poker.shuffle()  # 洗牌
    nicknames = ['player1', 'player2', 'player3', 'player4']
    players = [Player(nickname) for nickname in nicknames]
    for player in players:
        for _ in range(13):
            card = poker.deal()
            player.get_one_card(card)
        player.arrange()
        player.show()
    print('-'*20)


if __name__ == '__main__':
    main()
    main_pro()
