"""
定义描述三角形的类，提供计算周长和面积的方法

我们在类里面写的函数，通常称为方法，他们基本上都是给对象发消息。
但是有的时候，我们的消息并不想发给对象，而是希望发给这个类（类本身也是一个对象）
这个时候我们可以是由静态方法或者类方法
静态方法 - 发给类的消息  ---> @staticmethod --->装饰器
类方法 - 发给类的消息 ---> @classmethod ---> 装饰器 ---> 第一个参数（cls）是接收消息的类
"""


class Triangle:

    def __init__(self, a, b, c):
        # if a+b > c and a+c > b and b+c > a:  # 判断是否能够构成三角形，但这种写法是不正确的。
        #     self.a = a
        #     self.b = b
        #     self.c = c
        # else:
        #     raise ValueError("无效的边长")
        if not Triangle.is_valid(a, b, c):  # 不是最佳选择
            raise ValueError('无效的边长')
        self.a = a
        self.b = b
        self.c = c

    # def is_valid(self, a, b, c):  # 当调用三角形对象时，说明三角形已经能被构成
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    # @classmethod
    # def is_valid(cls, a, b, c):
    #     return a+b > c and a+c > b and b+c > a

    def C(self):
        return self.a + self.b + self.c

    def S(self):
        half = self.C() / 2
        return (half * (half - self.a) * (half - self.b) * (half - self.c)) ** 0.5


"""
边长无效会引发ValueError异常，出现异常后，如果没有try...except结构，程序会直接崩溃，如果有except捕获到了异常，代码直接转到except处执行。
如果try中的代码没有发生异常，或者发生了异常但是except没有捕获到，就不会执行except里的代码。
"""
if __name__ == '__main__':
    """"""
    try:
        t = Triangle(1, 2, 3)
        print(t.C())
    except ValueError as err:
        print(err)

if __name__ == '__mian__':
    if Triangle.is_valid(1, 2, 4):
        t = Triangle(1, 2, 4)
        print(t.C())
        print(t.S())
    else:
        print("无效的边长，无法构造三角形")
