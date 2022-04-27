"""
工资（月薪）结算系统
三类员工：
    - 部门经理：固定月薪，15000元
    - 程序员：计时结算月薪，每小时200元
    - 销售员：底薪+提成，底薪1800元，销售额5%提成

录入员工信息，自动结算月薪
"""


class Staff:

    def __init__(self):
        self.salary = None

    def get_salary(self):
        return self.salary


class Manager(Staff):

    def __init__(self):
        self.salary = 15000


class Programmer(Staff):

    def __init__(self, time):
        self.time = time
        self.salary = self.time * 200


class Salesman(Staff):

    def __init__(self, sales):
        self.sales = sales
        self.salary = self.sales * 0.05 + 1800


def main():
    position = int(input("输入职位 1。部门经理 2。程序员 3。销售："))
    if position == 1:
        manager = Manager()
        print(manager.get_salary(), "元")
    elif position == 2:
        time = int(input("输入工作时长："))
        programmer = Programmer(time)
        print(programmer.get_salary(), "元")
    elif position == 3:
        sales = int(input("输入销售额："))
        salesman = Salesman(sales)
        print(salesman.get_salary(), "元")


if __name__ == '__main__':
    main()