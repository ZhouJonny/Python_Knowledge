"""
字典 ---> 元素由键和值两部分构成，冒号前面的称为键，冒号后面的称为值，合在一起称为键值对
    * 键只能是不可变类型，使用哈希值来存储键
    * 值可以说string、list、set、dictionary
"""
student = {
    'id': '2015123221',
    'name': 'jonny.zhou',
    'favourites': ['eat', 'sleep'],
    'contacts': {
        'QQ': '904637097',
        'tel': '18360574109',
        'email': 'jonny.zhou@hp.com'
    }
}
print(student['name'])
# 值是list，则返回的是list
print(student['favourites'])
# 通过遍历得倒list中的每个元素
for fav in student['favourites']:
    print(fav)
# 值是字典，通过再次索引得倒值
print(student['contacts']['email'])