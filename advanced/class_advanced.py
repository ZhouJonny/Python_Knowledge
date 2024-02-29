# *** 类的实例状态是什么
"""
类的实例状态是指特定对象所包含的数据
当我们创建一个类的实例时，实例会继承类的属性和方法，同时也可以具有自己独特的属性值。
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 创建一个person类的实例
person1 = Person("jonny", "26")

# 输出实例的状态(即属性值)
print(person1.age)
print(person1.name)

# *** 属性装饰
"""
属性装饰器@property来创建一个只读属性，当类一个类被实例化之后，只读属性将不可更改
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

    # 一定要与属性同名
    def radius(self):
        return self._radius


class CircleProperty:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius


# 没有属性装饰的类实例化
circle = Circle(5)
# 没有属性装饰，要访问方法，需要使用方法调用
print(circle.radius())  # 输出5
# 直接访问属性，将会得到方法的引用而不是属性值
print(circle.radius)  # 输出<bound method Circle.radius of <__main__.Circle object at 0x7f78afc71430>>

# 有属性装饰的类实例化
circle_property = CircleProperty(5)
# 直接访问属性
print(circle_property.radius)  # 输出5
# 尝试修改属性值，会引发AttributeError
try:
    circle_property.radius = 10
except Exception as e:
    raise e