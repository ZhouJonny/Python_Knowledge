"""
字符串操作 - 字符串格式化
"""

a = 'hello, world'

# 居中
print(a.center(80, '@'))
# 右对齐
print(a.rjust(80, '#'))
# 左对齐
print(a.ljust(80, '$'))
# 零填充（在左边补0）
print(a.zfill(25))

# 格式化字符串的便捷语法
c = 123
d = 4567
print(f'{c}+{d}={c+d}')