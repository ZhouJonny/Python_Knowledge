"""
写一个函数，生成指定长度的验证码（数字和字母组成）
random库
    * choices ---> 会出现重复的元素
    * sample ---> 不会出现重复的元素
"""
import random
import string


def foo(n):
    """
    生成随机验证码

    :param n: 验证码的长度
    :return: 验证码
    """
    all_chars = string.ascii_lowercase + string.digits
    select_chars = random.sample(all_chars, n)
    return ''.join(select_chars)


print(foo(5))