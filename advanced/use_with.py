# how to use 'with'
# 上下文管理器用于管理资源的获取和释放，确保资源在使用完毕后能够正确地被释放，以避免资源泄漏等问题。
"""with操作文件
with open('filname', 'r') as f:
pass
"""

"""自己实现with的功能
__enter__ 和 __exit__ 是用于实现上下文管理器（Context Manager）的特殊方法。
进入with语句块时：调用__enter__
离开with语句块时：调用__exit__, __exit__一定要接收三个参数(exc_type, exc_value, traceback)
"""


# 实例1
class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return "Hello, context!"

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred with value {exc_value}")

        # 使用上下文管理器
        """
        在这个示例中，MyContextManager 类实现了 __enter__ 和 __exit__ 方法，
        当进入和离开 with 语句块时，相应的方法会被调用。
        在 with 语句块中，msg 变量会接收 __enter__ 方法返回的值，并在 with 语句块内被打印出来。
        """


with MyContextManager() as msg:
    print(msg)  # 输出__enter__的返回值, Hello, context!
    """输出结果
    Entering the context
    Hello, context!
    Exiting the context
    """


# 实例2
def connection():
    print("Connection")


def close():
    print("Close")
    return True


class MySQLDB():
    def __init__(self, host, port, username, password, database) -> None:
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database

    def __enter__(self):
        connection()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        close()
        return False

    def execute_sql(self, sql):
        print(f"Execute SQL: {sql}")


with MySQLDB(host='127.0.0.1', port=3300, username='tester', password='123456', database='test') as db:
    print(db)
    db.execute_sql("select * from database")


# 使用装饰器contextmanager