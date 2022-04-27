from abc import abstractmethod

"""
工资（月薪）结算系统
三类员工：
    - 部门经理：固定月薪，15000元
    - 程序员：计时结算月薪，每小时200元
    - 销售员：底薪+提成，底薪1800元，销售额5%提成

录入员工信息，自动结算月薪
"""
"""
子类对父类已有的方法，重新给出自己的实现版本，这个过程叫方法重写（override）。
在重写方法的过程中，不同的子类可以对父类的同一个方法给出不同的实现版本，那么该方法在运行时就会表现出多态性。
多态：给不同的对象发出同样的消息，不同的对象执行了不同的行为。
get_salary(self)就是方法的重写。
"""


class Staff:

    def __init__(self, no, name):
        self.no = no
        self.name = name

    """
    加个装饰器 @abstractmethod 说明此方法是抽象方法。 ---> from abc import abstractmethod
    抽象方法：
        这个方法暂时无法实现，专门留给子类去实现，子类必须要去实现，不同子类会有不同的实现版本。
    """

    @abstractmethod
    def get_salary(self):
        """抽象方法"""
        pass


class Manager(Staff):

    def get_salary(self):
        return 15000


class Programmer(Staff):

    def __init__(self, no, name):
        super().__init__(no, name)
        self.working_hour = 0

    def get_salary(self):
        return 200 * self.working_hour


class Salesman(Staff):

    def __init__(self, no, name):
        super().__init__(no, name)
        self.sales = 0

    def get_salary(self):
        return 1800 + 0.05 * self.sales


def main():
    staffs = [
        Manager(1, '刘备'),
        Programmer(2, '诸葛亮'),
        Salesman(3, '关羽'),
        Salesman(4, '张飞'),
        Programmer(5, '庞统'),
        Salesman(6, '马超')
    ]
    for staff in staffs:
        if type(staff) == Programmer:
            working_hour = int(input(f'请输入程序员{staff.name}本月工作时长：'))
            staff.working_hour = working_hour
        elif type(staff) == Salesman:
            sales = int(input(f'请输入销售{staff.name}本月销售额：'))
            staff.sales = sales
        print(f'{staff.name}本月工资是{staff.get_salary()}元')


if __name__ == '__main__':
    main()
