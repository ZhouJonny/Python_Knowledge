'''
输出1-100内的所有素数
'''
from math import  sqrt

def fun(x):
    end = int(sqrt(x))
    is_prime = True
    for i in range(2, end+1):
        if x % i ==0:
            is_prime = False
            break
    if is_prime:
        print(x)

for x in range(2, 101):
    fun(x)