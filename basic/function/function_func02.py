"""
位置参数和命名关键字参数
写一个函数，传入一个文件名（字符串），返回这个文件的后缀名。

hello.py ---> py/.py
hello.py.txt ---> txt/.txt
.abc --->没有后缀名，返回空字符串
abc. ---> 没有后缀名，返回空字符串
"""


def get_suffix_jonny(filename):
    suffix = filename.split('.')
    return suffix[-1]


# 定义函数时，写在 * 前的参数称为位置参数，调用函数传递参数时，只需要对号入座
# 写在 * 后面的参数称为命名关键字参数，调用函数传递参数时，必须要写成"参数名=参数值"的形式
def get_suffix(filename, *, has_dot=False):  # filename为位置参数， has_dot为关键字参数
    position = filename.rfind('.')
    # if position > 0:
    #     return filename[position+1:]
    # else:
    #     return
    if not has_dot:  # 是否需要 . ，函数调用参数为True时有.
        position += 1
    return filename[position:] if position > 0 else ' '  # 三目运算符


print(get_suffix('123.py'))  # 正确
# 调用函数传递参数时，可以给参数带上名字，这种参数称为关键字参数
print(get_suffix(has_dot=True, filename='123.py'))  # 正确
print(get_suffix('123.py', has_dot=True))  # 正确 ---> filename为位置参数， has_dot为关键字参数
print(get_suffix('123.py', True))  # 错误 ---> has_dot为关键字参数,不调用它无所谓，调用他一定要写关键字
