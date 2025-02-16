# python练习题
def dec(f):
    n = 3

    def wrapper(*arg, **kw):
        return f(*arg, **kw) * n

    return wrapper


@dec
def foo(n):
    return n * 2


# python练习题
class Rectangle:
    _count = 0

    def __init__(self, width, height):
        Rectangle._count += 1
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height


result = Rectangle(200, 100)


# python练习题
def abc(a, *, b, c):
    print(a, b, c)


abc(1, b=2, c=3)


# python练习题
def fn():
    t = []
    i = 0
    while i < 2:
        t.append(lambda x: print(i * x, end=","))
        i += 1
    return t


for f in fn():
    f(2)
