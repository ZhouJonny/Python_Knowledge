# 旨在总结异常处理机制


#try 语句
# try:
#     pass
# except Exception as e:
#     print(e)
# else:
#     print('successed')
# finally:
#     print('Finally block')


# 用try语句中的else分支    
def try_exception_else():
    """这里的else表示：try语句未抛出异常时，才执行else分支下的内容。
    """
    dic={
        "name": "panda",
        "age":"28"
    }
    try:
        dic['name']
    except KeyError:
        print("dict keyerror")
    else:
        # 业务逻辑
        print("successed")
        
        
#else与finally的区别
def try_exception_else_and_finally():
    """当程序遇到break，return语句，中断异常捕获，即使try语句未抛出异常，else中的逻辑也不会被执行，但会执行finally中的逻辑。
    """
    try:
        a = 1
        return a
    except Exception as e:
        print(e)
    else:
        print("successed")
    finally:
        print('finally')


  
