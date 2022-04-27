'''
打印如下所示的三角形图案：
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********
'''
row = int(input('inout row:'))
'''
for _ in range()
类似于c中：
for(int i=0;i<100;i++){
                        代码块
    }
    i只起到控制循环次数的作用，循环内的代码块并不会用到
'''
for i in range(row):
    for _ in range(i+1):
        print('*', end='')
    print()

print()

# 不会
for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(" ", end='')
        else:
            print("*", end='')
    print()

print()

# 不会
for i in range(row):
    for _ in range(row - i - 1):
        print(' ',  end='')
    for _ in range(2*i + 1):
        print("*", end="")
    print()