"""
文件操作

finally ---> 总是执行代码（不管正常异常，finally中的代码一定会被执行到）
"""
import sys

print(sys.getdefaultencoding())  # 获取系统默认编码
file = open('readme.txt', 'r', encoding='utf-8')
try:
    """
    当读取大文件的时候，应小部分小部分的读取（指定字符数），防止占用过多内存。
    文件很小，可以一次性读完。
    
    方法：
        先做一次读操作，判断读到数据了没有。
        如果读到数据，执行相应的操作，再继续读操作。
        如果没读到数据，则终止while循环。
    """
    # 如果读不到数据，read()就会返回None，None对应False，则while会终止循环。
    data = file.read(12)
    while data:
        print(data)
        data = file.read(12)
except:
    print("读文件时发生错误！")
finally:
    """总是执行代码"""
    file.close()