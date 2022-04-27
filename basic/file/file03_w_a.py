"""
文件操作（写文本文件）
"""


"""
w:
若文件不存在，会创建一个新的文件。
若文件存在，则会覆盖写。
"""
file = open('Data/temp.txt', 'w', encoding='utf-8')
try:
    """
    在字符串末尾加上 \n 才能换行写入
    """
    file.write("line1\n")
    file.write('line2\n')
    file.write('line3\n')
finally:
    file.close()

"""
a:
若文件不存在，会创建一个新的文件
若文件存在，会追加写。
"""
file = open('Data/temp.txt', 'a', encoding='utf-8')
try:
    file.write('line4\n')
    file.write('line5\n')
finally:
    file.close()

"""
以上代码等价于：
    上下文语法 ---> with
    进入和离开with的时候会自动执行某些操作。
    下面的写法在离开with上下文的时候，会自动执行file对象的close()方法
"""
with open('Data/temp.txt', 'a', encoding='utf-8') as file:
    file.write('上下文语法添加')