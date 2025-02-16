def fn():
    t = []
    i = 0
    while i < 3:
        t.append(lambda x: print(i * x, end=","))
        i += 1
    return t  # t是一个列表，t = [lambda x: print(i * x, end=","),lambda x: print(i * x, end=","),lambda x: print(i * x,
    # end=",")]


for f in fn():
    """
        对t进行遍历，t[0],t[1],t[2], i == 3。会进行3次遍历。
    """
    f(1)
    f(2)
