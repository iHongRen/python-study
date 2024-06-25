# 异常处理

# 异常: 程序运行过程中出现的错误
# 异常处理: 程序在出现错误时, 能进行相应的处理, 保证程序的健壮性

# 常见的异常
# 1. ZeroDivisionError: 除数为0
# 2. NameError: 引用一个不存在的变量
# 3. TypeError: 类型错误
# 4. ValueError: 值错误
# 5. IndexError: 索引超出范围
# 6. KeyError: 字典中没有该键
# 7. AttributeError: 对象没有该属性
# 8. ImportError: 导入模块失败
# 9. SyntaxError: 语法错误
# 10. ...

# 异常处理语法

# try-except
# 当 try 中的代码块发生异常时, 执行 except 后的代码块
# except 后跟异常类型, 表示捕获该类型的异常
# 多个 except 可以捕获不同类型的异常
try:
    ret = 10 / 0
except ZeroDivisionError:
    print("除数不能为0")
except NameError:
    print("变量不存在")


# 一个 except 可以捕获多个异常类型
# except 后跟元组, 表示捕获多个类型的异常
# as 后的变量名 e, 表示捕获到的异常实例
try:
    ret = 10 / 0
except (ZeroDivisionError, NameError) as e:
    print(type(e))  # 输出: <class 'ZeroDivisionError'>
    print(e)  # 输出: division by zero


# try-except-else
# 当 try 中的代码块没有发生异常时, 执行 else 后的代码块
try:
    ret = 10 / 5
except ZeroDivisionError:
    print("除数不能为0")
else:
    print("除法运算正常")


# try-except-finally
# 无论是否发生异常, 都会执行 finally 后的代码块
try:
    ret = 10 / 0
except ZeroDivisionError:
    print("除数不能为0")
finally:
    print("无论是否出现异常, 都会执行该代码块")


# try-except-else-finally
# 当 try 中的代码块没有发生异常时, 执行 else 后的代码块
# 无论是否发生异常, 都会执行 finally 后的代码块
try:
    ret = 10 / 0
except ZeroDivisionError:
    print("除数不能为0")
else:
    print("除法运算正常")
finally:
    print("无论是否出现异常, 都会执行该代码块")



# 抛出异常 raise
# 当程序遇到错误时, 可以手动抛出异常, 然后交给调用者处理
# 抛出异常的语法: raise 异常类型(异常信息)

# 在自定义函数 divide() 中, 当除数 b 为0时, 手动抛出 ZeroDivisionError 异常
# 抛出异常后, 后面的代码不会执行, 也就是 return a / b 不再执行
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

# 使用 try-except 捕获异常, 并处理 print(e)
try:
    ret = divide(10, 0)
except ZeroDivisionError as e:
    print(e)



# 自定义异常
# 继承自 Exception 类
class MyException(Exception):
    def __init__(self, message):
        self.message = message

try:
    num = 0
    if num==0:
        raise MyException("抛出自定义异常信息")
    ret = 10 / num
except MyException as e:
    print(e.message)


# 使用装饰器处理异常
# 装饰器是一种函数, 可以用来装饰其他函数, 用于添加额外的功能
# 定义一个装饰器函数, 用于处理异常
# 这种方式可以更好地分离异常处理逻辑,提高代码的可重用性。
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"发生异常了: {e}")
    return wrapper

# 使用装饰器处理 divide() 函数中的异常
@handle_exceptions
def divide(a, b):
    return a / b

divide(10, 0)


# with 语句
# with 语句可以确保资源在使用完毕后被正确地关闭或清理, 即使在处理过程中发生异常。
# with 语句可以用来简化文件操作、数据库连接等资源的打开和关闭过程。
# 打开文件时, with 语句可以自动关闭文件, 无需手动调用 close() 方法
# with 语句可以简化代码, 提高代码的可读性

try:
    f = open("file.txt", "r")
    print(f.read())
except Exception as e:
    print(e)  # 输出: file.txt: No such file or directory
finally:
    try:
        f.close()
    except Exception as e:
        print(e) # 输出: name 'f' is not defined


# 使用 with 语句简化上述代码, 无需手动调用 close() 方法

try: 
    with open("file.txt", "r") as f:
        print(f.read())
except Exception as e:
    print(e) #  输出: No such file or directory: 'file.txt'

# 断言 assert
# assert 断言语句, 用于判断表达式的真假
# 如果表达式为真, 则继续执行后面的代码
# 如果表达式为假, 则抛出 AssertionError 异常
# assert 断言语句可以添加参数, 用于自定义异常信息
# 基本语法: assert 表达式, 异常信息
def divide(a, b):
    assert b != 0, "抛出断言异常，因为除数为0" # b==0时, 会抛出异常
    return a / b

print(divide(10, 2)) # 输出: 5.0

try:
    divide(10, 0)
except AssertionError as e:
    print(e) # 输出: 抛出断言异常，因为除数为0
