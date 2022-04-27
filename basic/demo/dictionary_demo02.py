"""
字典中保存了股票的信息，完成以下操作：
1。找出股票价格大于100元的价格，并创建一个新的字典
2。找出价格最低和最高的股票对应的股票代码
3。按照股票价格从高到底给股票代码排序
"""
stocks = {
    'APPL': 191.88,
    'GOOG': 1890.1,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 188.44,
    'FB': 208.09,
    'SYMC': 21.29
}
# 1。找出股票价格大于100元的价格，并创建一个新的字典
# 方法1
stocks_over100_func1 = {}
for key, value in stocks.items():
    if value > 100:
        stocks_over100_func1[key] = value
print(stocks_over100_func1)
# 方法2(推荐) ---> 生成式
stocks_over100_func2 = {key: value for key, value in stocks.items() if value > 100}
print(stocks_over100_func2)

# 2。找出价格最低和最高的股票对应的股票代码
# 例子
"""
两两配对，压成二元组。以少的那个为主，E没有配对对象，则被丢弃
"""
for x in zip('ABCDE', [1, 2, 3, 4]):
    print(x)
# 以下两种写法等价
dict1 = dict(zip('ABCDE', [1, 2, 3, 4]))
dict2 = dict(A=1, B=2, C=3, D=4)
# ----------------------------------
# 方法1(zip()函数) ---> 转化为list
# tip:使用zip()函数，将字典的键值互换
dict_reserve = dict(zip(stocks.values(), stocks.keys()))
print(dict_reserve)
max_stock = max(dict_reserve.keys())
min_stock = min(dict_reserve.keys())
print(f'价格最高的股票：{dict_reserve[max_stock]}  价格最低的股票：{dict_reserve[min_stock]}')
# 方法2(zip()函数) ---> 转化为tuple
"""
zip()函数会生成若干对二元组
使用二元组比大小，先比较第一个元素的大小，若一样大，再比较第二个元素。
min(zip(stocks.values(), stocks.keys()) 返回的是(value，key)的二元组
"""
_, max_code = max(zip(stocks.values(), stocks.keys()))  # 得到value即股票价格最大的二元组，只取股票代码
print('最大'+max_code)
print('最小'+min(zip(stocks.values(), stocks.keys()))[1])  # 上面两行是折行的拆解写法
# 方法3(zip()函数) ---> max()高级用法
"""
max(stocks) 比的是每一个键的大小
max(stocks, key= stock.get) max()函数的关键字设为值，则比较的是值的大小，返回的是字典中的键
"""
# 例子
fruits = ['zpple', 'pear', 'peach', 'watermelon']
print(max(fruits))  # 会按首字母来排序
print(max(fruits, key=len))  # 添加关键字len，则会以字母长度来比较
# 使用max()高级用法，对字典进行排序， key=stocks.get
print('max：'+max(stocks, key=stocks.get))  # 以stocks.get进行排序，即以字典中的值，返回的是字典中的键
print('min:'+min(stocks, key=stocks.get))

# 3。按照股票价格从高到底给股票代码排序
# sort()方法的高级形态 ---> sorted()函数，用法同max()
sort_stocks = sorted(stocks, key=stocks.get, reverse=True)
new_stocks = {stock: stocks[stock] for stock in sort_stocks}
print(new_stocks)


