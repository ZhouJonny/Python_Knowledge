"""
创建对象/给对象发消息
step1：导入模块
step2：创建对象 ---> 构造器语法 ---> 类名(..., ...)
step3：给对象发消息（调用对象的方法）
"""
# step1
from class01 import Student

# step2
stu1 = Student('name1', 17)
stu2 = Student('name2', 18)

# step3
stu1.study("python")  # stu1就是Student类的self
stu1.eat()

stu1.age_xx()
stu1.age = 20
stu1.age_xx()
