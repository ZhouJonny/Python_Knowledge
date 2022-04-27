"""
字符串操作 - 解码和编码

str(字符串) ---> encode() ---> bytes(字节串)
bytes(字节串) ---> decode() ---> str(字符串)

UTF-8是一种变长编码
表示数字和英文字母的时候，只需要1个字节
表示中文的时候，需要3个字节
表示Emoji字符的时候，需要4个字节
"""
a = '我爱你中国'
b = a.encode('utf-8')
print(type(b))
print(b, len(b))
# 将b记录下来，此时b是utf-8的解码, 把b赋给c
c = b'\xe6\x88\x91\xe7\x88\xb1\xe4\xbd\xa0\xe4\xb8\xad\xe5\x9b\xbd'
# 如果编码和解码的方式不一样，python中可能会产生UnicodeDecodeError异常，也有可能会产生乱码
print(c.decode('gbk'))