'''
判断年份是不是闰年
'''
year = int(input("输入年份："))
if(year%4 == 0 and year%100 != 0):
    print("%d是闰年"%year)
else:
    if(year%400 == 0):
        print("%d是闰年"%year)
    else:
        print("%d不是闰年"%year)

'''输入年份，闰年返回true，否则返回false'''
is_leap = year%4==0 and year%100!=0 or year%400==0
print(is_leap)
'''比较运算符会产生布尔值，而逻辑运算符and和or会对这些布尔值进行组合，最终也是得到一个布尔值，闰年输出True，平年输出False'''