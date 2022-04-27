'''
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积
'''
a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a+b > c and a+c>b and b+c > a:
    print(f'周长：{a+b+c}')
    p = (a+b+c)/2
    print(f'面积:{p*(p-a)*(p-b)*(p-c)}')  # 海伦公式
else:
    print('无法构成三角形')