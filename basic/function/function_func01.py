"""
局部变量和全局变量

在函数里面定义的变量称为局部变量，和全局变量没有任何关系，各自都不影响。
在python中搜索一个变量是按照LEGB的顺序搜索的。
Local -> Embedded -> Global -> Build-in -> NameError: name not define
"""
x = 100  # 全局变量


def foo():
    # 如果不想在foo()中定义局部变量x，而是直接使用全局变量x，应该怎么做？？
    # global x  ---> 在foo()改变x的值，即改变了全局变量x的值
    x = 200  # foo()的局部变量，也是bar()的嵌套变量

    def bar():
        # 如果不想在bar()中d定义局部变量x，而是直接使用嵌套作用域中的x，应该怎么做？？
        # nonlocal x   ---> 在bar()中改变x的值，即改变了foo()里x的值
        x = 300
        print(x)  # 输出bar()局部变量 x=300

    bar()
    print(x)  # 输出局部变量

foo()
print(x)  # 输出全局变量