import time


# 1.log
# 在执行函数前后记录日志
def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[{func.__name__}] is running ...")
        result = func(*args, **kwargs)
        print(f"[{func.__name__}] is finished.")
        return result

    return wrapper


@log_decorator
def test_log_decorator(x):
    return x + x


print(test_log_decorator(6))


# 2.性能测试
# 使用装饰器记录函数的执行时间，有助于性能的分析和优化
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[{func.__name__}] use {end_time - start_time} s")
        return result

    return wrapper


@timing_decorator
def test_timing_decorator():
    time.sleep(2)


test_timing_decorator()


# 3.控制访问
# 装饰器可以用来增加访问控制逻辑，例如验证用户权限
def admin_required(func):
    def wrapper(*args, **kwargs):
        if not user_is_admin():
            raise Exception("用户不是管理员，无法执行该操作！")
        return func(*args, **kwargs)

    return wrapper


def user_is_admin():
    # 这里写检查用户是否为管理员的逻辑
    return True


@admin_required
def test_admin_required():
    print("sensitive function")


test_admin_required()


# 4.缓存结果
# 装饰器可以用于缓存函数的结果，避免重复计算，特别是在处理昂贵的计算任务时。
def cache_decorator(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return wrapper
