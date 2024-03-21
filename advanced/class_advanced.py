# title 类的实例状态是什么
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

# title 属性装饰@property
"""
属性装饰器@property来创建一个只读属性，当类一个类被实例化之后，只读属性将不可更改
"""


class Circle:
    def __init__(self, radius):
        self._radius = radius

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
    print(e)

# title 静态方法@staticmethod/类方法@classmethod
"""
使用@staticmethod装饰器可以将一个方法定义为静态方法，这意味着它不会接收隐式的self参数，并且可以通过类或实例直接调用。
静态方法通常用于不需要访问实例状态的功能性方法。
使用@classmethod装饰器可以将一个方法定义为类方法。类方法的第一个参数通常被命名为cls，它表示类本身而不是实例。
类方法可以通过类或实例调用，并且可以防伪类的属性和调用其他类方法。
两个概念：
    1、创建类的实例
    2、不创建类的实例
"""

"""1、创建类的实例
通俗的来说，就是在类民后面加上括号，并且根据类的构造函数(__init__方法)的定义，传入必要的参数。
这样做的话，会创建该类的一个对象（实例），之后就可以使用这个实例来调用类中定义的实例方法。
这些方法可以访问或修改对象的状态（即实例变量）
"""


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        return f"{self.model}{self.make}"


# 创建类的实例
my_car = Car("Tesla", "model3")
print(my_car.display_info())  # 使用实例调用实例方法

"""2、不创建类的实例
指的是直接使用类名来调用类中定义的静态方法或类方法。
静态方法和类方法都是通过装饰器（@staticmethod或@classmethod）定义的，它们不依赖于类的实例。
因此，不需要创建一个类的实例就可以调用它们。
静态方法不接受类或实例的隐式第一个参数，而类方法接收类作为隐式第一个参数（通常命名为cls）

*** self 与 cls：
        对于一个类Employee，self可以理解为Employee(), cls可以理解为Employee
"""


# 2.1 使用静态方法
class MathOperations:
    def __init__(self):
        pass

    @staticmethod
    def square(x):
        return x ** 2


# 使用静态方法，不创建类的实例，直接调用静态方法
print(MathOperations.square(2))


# 2.2 使用类方法
class Employee:
    num_of_employees = 0  # 类变量，用于追踪员工数量

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_employees += 1

    @classmethod
    def get_num_of_employee(cls):
        return f"Total number of employees: {cls.num_of_employees}"

    @classmethod
    def create_from_string(cls, employee_str: str):
        name, salary = employee_str.split("-")
        return cls(name, int(salary))  # cls相当于Employee类的一个占位符。cls与Employee是等价的。


print(Employee.get_num_of_employee())  # 输出0

emp_str = "jonny-100000"
new_emp = Employee.create_from_string(emp_str)

print(new_emp.name)
print(new_emp.salary)
print(Employee.get_num_of_employee())  # 输出1

emp_str_1 = "chris-100000"
new_emp_1 = Employee.create_from_string(emp_str_1)

print(new_emp_1.name)
print(new_emp_1.salary)
print(Employee.get_num_of_employee())  # 输出2


# 衍生：用类方法来创在实例。
