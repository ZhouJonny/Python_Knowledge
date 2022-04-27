"""
文件操作（读取二进制文件（字节文件））
"""
# rb ---> read bite 读二进制文件
file = open('Data/ScreenShot.png', 'rb')
"""
seek(0, 2)
    移动文件指针，将文件指针从初始位置移动到文件末尾。
    0：文件初始位置，2：文件结束位置，1：文件指针当前位置
tell()
    查看文件指针移动的字节数

两个方法结合在一起，即可获得文件大小
"""
file.seek(0, 2)
print(file.tell())
# 将文件指针移动到初始位置
file.seek(0, 0)
try:
    """
    512通常是操作系统分配的最小文件分区，每次读512效率最高
    """
    data = file.read(512)
    while data:
        print(data, end='')
        data = file.read(512)
finally:
    file.close()