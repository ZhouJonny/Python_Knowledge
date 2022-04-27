from enum import Enum
"""
__ __: 魔术方法（魔法方法）---> 有特殊用途和意义的方法
    __init__: 初始化方法，在用构造器语法创建对象的时候会被自动调用
    __str__:获得对象的字符串表示，在调用print()输出对象时会被调用
    __repr__:获得字符串的字符串表示，把对象放到容器中，调用print输出时会自动调用
!!! __lt__:
    __slots__:如果限制一个类的对象只能拥有某些属性，可以在类中使用__slots__魔法方法

枚举类型：
    如果一个变量的取值只有有限个选项，可以考虑使用枚举类型。
    python中没有定义枚举类型的语法，但是可以继承Enum类来实现枚举类型。
    结论1：枚举类型是定义符号常量的最佳选择！！！
    结论2：符号常量（有意义的名字）总是优于字面常量
    符号常量：没有直接写0，1，2，3， 而是写四个符号常量SPADE, HEART, CLUB, DIAMOND来代表0，1，2，3。增加代码可读性。
"""
"""
初始化一床扑克牌
"""


# 枚举类型
class Suite(Enum):
    """
    枚举类型, 见poker04.py
    写一个类来继承Enum，在里面定义符号常量。
    这样，想表示花色的时候，就可以用这四个符号，这四个符号还有其对应的值。
    增强代码的可读性，其他没什么作用
    """
    # SPADE, HEART, CLUB, DIAMOND = 0, 1, 2, 3
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:

    def __init__(self, suite: Suite, face: int):  # 这种称为类型标注，：后面的是变量的类型
        """
        初始化方法

        :param suite: 花色
        :param face: 点数
        """
        self.face = face
        self.suite = suite

    def __str__(self):
        return self.show

    # __repr__功能包含了__str__的功能
    def __repr__(self):
        return self.show

    def __lt__(self, other):  # self表示自己，other表示另一张牌
        """
        按花色排序
        花色相同则比点数
        ord() ---> 返回对应的 ASCII 数值

        :param other:
        :return:
        """
        if self.suite == other.suite:
            return self.face < other.face
        # return ord(self.suite) < ord(other.suite)
        return self.suite.value < other.suite.value

    @property
    def show(self):
        # suites = {'S': '♠️', 'H': '♥️', 'C': '♣️', 'D': '♦️'}
        suites = ['♠️', '♥️', '♣️', '♦️']
        faces = [' ', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        # return f'{suites[self.suite]}{faces[self.face]}'
        """
        self.suite.value --->0,1,2,3 就是将符号常量转化为字面常量
        """
        return f'{suites[self.suite.value]}{faces[self.face]}'


def main():
    """程序入口"""
    card1 = Card(Suite.CLUB, 1)
    card2 = Card(Suite.SPADE, 13)
    card3 = Card(Suite.HEART, 9)
    card4 = Card(Suite.DIAMOND, 11)
    print("show" + card1.show, card2.show, card3.show, card4.show)
    print("card1 和 card2一样？" + str(card1 is card2))
    card1 = card2
    print("card1 和 card2一样？" + str(card1 is card2))
    print(card1, card2, card3)  # 调用__str__魔术方法，输出的不是card1在内存的地址，而是引用的对象。__repr__也可以实现同样的功能。
    print([card1, card2, card3, card4])  # 调用__repr__魔术方法


if __name__ == "__main__":
    main()  # 代码要这么写：要执行的语句放在main()里，然后在这里调用main()
