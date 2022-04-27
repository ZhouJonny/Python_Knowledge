'''
用模块管理函数
'''


def foo():
    print("foo1")


def foo():
    print("foo2")

# 当命名冲突的时候，由于python没有重载的概念，那么后面定义的函数将会覆盖掉前面定义的函数
# 意味着同名函数只有最后一个函数才是真正存在的
foo()