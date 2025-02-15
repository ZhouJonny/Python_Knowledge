# 冒泡排序
def double_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


my_list = [12, 34, 65, 11]
print(double_sort(my_list))
