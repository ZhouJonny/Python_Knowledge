"""
记录一个班级里五名学生的三门课成绩

* 嵌套列表的生成 [[] for _ in range(3)] --->[[], [], []]
* 让嵌套列表也有元素 [[random.randrange(50, 101) for _ in range(3)] for _ in range(5)]
* 获取嵌套列表每行的元素 ---> scores[i] 第i行所有元素
* 获取嵌套列表每列的元素 ---> 两个嵌套列表
    for j in range(len(列))
        for i in range(len(行))
            print(scores[i][j]])  # 输出第j列的i个元素
"""
import random

names = ['关羽', '张飞', '赵云', '黄盖', '马超']
courses = ['语文', '数学', '英语']
# scores[0] 会输出第一行所有的元素
# scores[0][0] 会输出第一行第一列的元素
# scores = [[100, 100, 99],
#           [89, 100, 31],
#           [34, 54, 75],
#           [67, 76, 45],
#           [65, 78, 64]]
# 随机生成上述列表
# 例子：for [[] for _ in range(3)]
scores = [[random.randrange(50, 101) for _ in range(len(courses))]
          for _ in range(len(names))]
print(scores)
# 使用enumerate() 枚举函数， 对应的i，j即是scores嵌套列表的下标
for i, name in enumerate(names):
    for j, course in enumerate(courses):
        print(f'{name}的{course}成绩：{scores[i][j]}')

# 统计每个学生的平均成绩
for i, name in enumerate(names):
    print(f'{name}的平均成绩是{sum(scores[i]) / len(courses) :.1f}')

# 统计每门课程的最高分和最低分
for j in range(len(courses)):
    print(f'{courses[j]}的最高分{max([scores[i][j] for i in range(len(names))])}')
    print(f'{courses[j]}的最低分{min([scores[i][j] for i in range(len(names))])}')
