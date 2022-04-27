"""
继承：
    从已经有的类进行扩展，创建出新的类，这个过程就叫继承。
    继承是实现代码复用的一种手段，但是千万不要滥用继承，找不到is-a关系的时候！
    提供继承信息的叫做父类（超类，基类），得到继承信息的类称为子类（派生类）。---> 子类比父类更加强大！
    有了继承就不需要写一些重复的代码，而是写这个类特有的功能。
继承是一种is-a关系：
    a student is a person
    a teacher is a person

子类直接从父类继承公共的属性和行为，再添加自己特有的属性和行为。
子类对父类已有的方法，重新给出自己的实现版本，这个过程叫方法重写（override）。
在重写方法的过程中，不同的子类可以对父类的同一个方法给出不同的实现版本，那么该方法在运行时就会表现出多态性。
多态：给不同的对象发出同样的消息，不同的对象执行了不同的行为。

所以子类一定是比父类更强大的，任何时候都可以用子类对象去替代父类对象。

python中的继承允许多重继承，一个类可以有一个或多个父类。
如果不是必须使用多重继承的场景下，请尽量使用单一继承。
"""


class Person:
    """人"""

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def eat(self):
        print(f"{self.name} is eating")

    def play(self, game_name):
        print(f'{self.name} is playing {game_name}')


class Student(Person):
    """学生"""

    def __init__(self, name, gender, grade: int):
        self.name = name
        self.gender = gender
        self.grade = grade

    def study(self, course_name):
        print(f'{self.name} is studying {course_name}')


class Teacher(Person):

    """老师"""
    def __init__(self, name, gender, title):
        """
        省去：
            self.name = name
            self.gender = gender
       super().__init__(name, gender) ---> 就是拿到父类的初始化方法,效果同上
        """
        super().__init__(name, gender)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title} is teaching {course_name}')


stu = Student('jonny', 'F', 4)
stu.eat()
stu.study('python')

teacher = Teacher('周老师', 'M', '叫兽')
teacher.play('lol')
teacher.teach('python')
