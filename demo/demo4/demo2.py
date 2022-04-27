'''
输入两个正整数，计算它们的最大公约数和最小公倍数。
    两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。
    最小公倍数= x*y // 最大公约数
'''
x = int(input('first number:'))
y = int(input('second number:'))
# 如果x大于y，就交换x与y的值
if x > y:
    x, y = y, x  # 将x赋值给y，y赋值给x
# 从两个数中较小的那个开始做递减循环
for factor in range(x, 0, -1):  # 从大到小循环，记得加步长！！
     if x % factor == 0 and y % factor == 0:
         print(f'最大公约数{factor}')
         print(f'最小公倍数{x*y // factor}')