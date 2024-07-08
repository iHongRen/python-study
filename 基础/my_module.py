# 定义一个类
class MyClass:
    def my_method(self):
        print("这是模块内的类方法")

# 定义一些变量
my_variable = "这是模块内的一个变量"
PI = 3.14159
GRAVITY = 9.8

# 定义一些函数
# 定义一个模块
def my_function():
    print("这是模块内的函数")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# 设置 __all__ 变量，只导入指定的变量、函数或类
# 在使用 from my_module import * 导入时，
# 只导入以下内容：
__all__ = ['my_function', 'MyClass']

