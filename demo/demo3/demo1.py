"""
英制单位英寸与公制单位厘米互换。
"""
value = float(input("请输入长度："))
unit = input("请输入单位：")
if unit == "in" or unit == "英寸":
    print(f"{value}in = {value*2.54}cm")
elif unit == "cm" or unit == "厘米":
    print(f"{value}cm = {value/2.54}in")

'''
如果condition2 是 condition1 的补集：
if condition1:
    ...
else:
    ...
用if-else

如果condition1 和 condition2 没有关系：
if condition1:
    ....
elif condition2:
    ....
用if-elif
'''