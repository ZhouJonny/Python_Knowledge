"""
输入一段话，统计每个英文字母出现的次数
"""
# 方法1
"""
使用get()函数，通过key来取value，若key不存在则使用默认值作为value。
"""
sentence = input('输入一段字母：')
count = {}
for ch in sentence:
    if 'A' <= ch <= 'B' or 'a' <= ch <= 'z':
        count[ch] = count.get(ch, 0) + 1
for key, value in count.items():
    print(f'{key}出现的次数：{value}')

# 方法2
"""
使用string库里的所有小写字母 ---> string.ascii_lowercase
用字典生成式创建小写字母的字典，初始键值为0
"""
import string
dist1 = {letter: 0 for letter in string.ascii_lowercase}
content = sentence.lower()  # 全部变成小写
for item in content:
    if item in dist1:
        dist1[item] += 1
for key, value in dist1.items():
    print(f'{key}出现的次数是{value}')