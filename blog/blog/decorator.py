# coding=utf-8
# 装饰器文件
from functools import wraps


# 装饰器文件
def method_examine(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            print("方法发生错误了：%s" % e)

    return wrapper
