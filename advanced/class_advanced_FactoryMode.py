"""
假设我们有一个Employee类，此外还有两个子类Manager类和Developer类。
实现根据传入的职位信息自动决定创建Manager类还是Developer类。
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def working(self):
        return f"{self.name} is working"

    @classmethod
    def create(cls, name: str, salary: int, position: str):
        if salary < 0:
            raise ValueError("Salary cannot be negative")

        if position.lower() == "manager":
            return Manager(name, salary)
        elif position.lower() == "developer":
            return Developer(name, salary)
        else:
            return cls(name, salary)

        # 用match-case 实现上述功能
        # match


class Manager(Employee):
    def working(self):
        return f"{self.name} is managing"


class Developer(Employee):
    def working(self):
        return f"{self.name} is developing"
