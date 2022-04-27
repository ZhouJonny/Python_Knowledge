"""
字符串操作 - 修剪、替换字符串
* strip() ---> 修剪字符串左右两端的空格
* lstrip() ---> 修剪左端空格
* rstrip() ---> 修剪右端空格
* replace() ---> 替换，若并不是修改原来的字符串，而是将替换后的内容返回给你。如果想拿到这个内容，可以重新赋值。
"""
email = ' jonny.zhou@hp.com '
tel = ' 183 6057 4109 '
content = ' jonny.zhou '
# 修剪字符串左右两端的空格，中间的空格不会被修剪
print(email.strip())
print(tel.strip())
# 修剪字符串左端的空格
print(email.lstrip())
# 修剪字符串右端的空格
print(tel.rstrip())

# 将指定的字符串替换成新的内容，可以在一个变量后面跟多个方法
print(content.strip().replace('jonny', '*').replace('zhou', '#'))