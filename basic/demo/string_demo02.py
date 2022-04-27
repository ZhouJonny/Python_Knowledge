"""
随机生成4位验证码
"""
import random
import string

# 使用string库，得到数字和大小写字母
all_chars = string.ascii_letters + string.digits
print(all_chars)

for _ in range(10):
    select_chars = random.choices(all_chars, k=4)
    print(''.join(select_chars))