"""
字符串操作 - 字符串的拆分和合并
* split() ---> 默认以空格拆分成列表
* join() ---> 将列表合并成字符串
"""
content = 'you go your way, I will go mine.'
# 将, 与 . 都替换成 _ 空格
contents = content.replace(',', '').replace('.', '')
# split() ---> 默认以空格拆分字符串，得到一个列表
words = contents.split()
print(words, len(words))
for word in words:
    print(word)

# maxsplit ---> 限制拆分最大次数
words = contents.split(' ', maxsplit=4)
print(words, len(words))

# 从由向左拆分字符串，最多拆4次
words = contents.rsplit(' ', maxsplit=4)
print(words, len(words))

# split(',') ---> 以 , 拆分字符串
items = content.split(',')
for item in items:
    print(item)

# 合并，将列表中的元素用指定的字符串连接起来
poetry = ['床前明月光', '疑是地上霜', '举头望明月', '低头思故乡']
print('&'.join(poetry))