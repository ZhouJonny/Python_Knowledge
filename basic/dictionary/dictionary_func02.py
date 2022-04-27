"""
 字典的运算 --- 成员运算、下标运算
"""
student = {
    'name': 'jonny',
    'sex': True,
    'id': '2015123221',
    'city': 'Shanghai',
}

# 字典的索引放在赋值运算符的左边
# 如果索引对应的键是存在的，就更新它的值
student['name'] = 'name1'
student['sex'] = False
# 如果字典中没有对应的索引，就新增加一组键值对
student['age'] = 24
print(student)

# 成员运算 ---> in
print('name' in student)
print('age' in student)

# 取值 ---> 推荐使用get()函数
# 若字典里有name键，则直接输出name对应的值 ---> 如果要使用下标运算，一定要保证键一定存在！
print(student['name'])
# 若字典里没有score键，则程序崩溃！高危行为！！ ---> KeyError: 'score'
# print(student['score'])
# 解决办法: 1。 用try except
#          2。 用get()函数 ---> 通过key获取value，若key不存在，不会发生KeyError错误，而是得到一个None或者你指定的默认值
print(student.get('score'))
# 拿不到score时，给个默认值
print(student.get('score', 360))

# 删除键值对
"""
两者区别：
    * del 不会返回任何东西，直接删除
    * pop() 会将删除的键值对的值返回
"""
del student['name']
student.pop('age')