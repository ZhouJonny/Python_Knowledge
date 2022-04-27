"""
字符串的操作方法

*！！： string类型是不可变类型
变形：
    * upper() ---> 所有字母大写
    * lower() ---> 所有字母小写
    * capitalize() ---> 一句话的首字母大写
    * title() ---> 一句话中，每个单词的首字母都大写
判断：
    isdigit() ---> 是否纯数字
    isalpha() ---> 是否纯字母
    isalnum() ---> 是否数字或字母构成
    isascii() ---> 是否由ascii码构成
    startswith('字符/字符串') ---> 判断字符串是否以特定的 字符/字符串 开头
    endswith('字符/字符串') ---> 判断字符串是否以特定的 字符/字符串 结尾

"""

a = 'i, LOVE, you'

# 所有字母大写
print(a.upper())
# 所有字母小写
print(a.lower())
# 一句话的首字母大写
print(a.capitalize())
# 每个单词的首字母大写
print(a.title())

# 是否纯数字构成
print(a.isdigit())
# 是否纯字母构成
print(a.isalpha())
# 是否只由数字或字母构成
print(a.isalnum())
# 是否由ascii码构成
print(a.isascii())
b = "你好呀"
# 判断字符串是否以 你好  开头
print(b.startswith('你好'))
# 判断字符串是否以 啊 结尾
print(b.endswith('啊'))