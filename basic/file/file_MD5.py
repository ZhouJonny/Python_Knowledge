"""
MD5:5dd5087f4eec2be635b1966330db5b74
"""
from hashlib import md5, sha256


hasher = md5()
hasher2 = sha256()
file = open('/Users/zhouyujie/Desktop/python-3.10.4-macos11.pkg', 'rb')
try:
    data = file.read(512)
    while data:
        # 更新MD5对象的数据
        hasher.update(data)
        hasher2.update(data)
        data = file.read(512)
finally:
    file.close()
# 获得十六进制形式的MD5值
print(hasher.hexdigest())
# 获得十六进制形式的SHA256值
print(hasher2.hexdigest())