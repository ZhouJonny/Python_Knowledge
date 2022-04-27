"""
两个类之间有哪些可能的关系？
～ is-a关系：继承 ---> class Student(Person):
    - 子类直接从父类继承公共的属性和行为，再添加自己特有的属性和行为。
    - a student is a person
～ has-a关系：关联
    - 把一个类的对象当成另外一个类的对象属性
    - 分为普通关联和强关联（整体和部分的关联）
    Poker-Card: 扑克有52张牌
    Student-Computer：学生有笔记本电脑
    - a person has a identity card
～ use-a关系：依赖
    - 一个类的对象作为另外一个类的方法的参数或返回值
    - a person use a  vehicle
"""


class Vehicle:
    """父类"""
    pass


class Horse(Vehicle):
    """
    继承：
    Horse类继承Vehicle类
    """
    pass


class Follower:
    """徒弟"""
    def __init__(self, name):
        self.name = name


class MrTang:

    def __init__(self):
        """
        关联：
        唐僧有三个徒弟
        Follower类是MrTang类的一个属性，并且可以多次实例化Follower类放在列表中。
        """
        self.followers = [Follower("孙悟空"), Follower("猪八戒"), Follower("沙和尚")]

    def drive(self, horse):
        """
        依赖：
        唐僧骑白马
        """
        pass
