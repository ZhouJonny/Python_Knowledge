'''
输入一个正整数判断是不是素数
    素数指的是只能被1和自身整除的大于1的整数
'''
from math import sqrt

x = int(input('输入一个正整数:'))
end = int(sqrt(x))
is_prime = True

for i in range(2, end+1):  # 2-平方差 都不能被x除尽
    if x % i == 0:
        is_prime = False
        break

if is_prime and x != 1:
    print("素数！")
else:
    print("不是素数！")