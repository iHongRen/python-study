# 函数

""" 
函数定义语法：其中返回类型部分可省略
def 函数名（参数列表）-> 返回类型:
    函数体
    return 返回值
"""

# 最小函数
def _(): pass
print(type(_)) # <class 'function'>


# 定义一个函数，用于计算两个数的和
def add(a, b):
    return a + b

# 调用函数
result = add(1, 2)
print(result)  # 输出：3

# 也可以增加参数类型和返回类型
def add(a: int, b: int) -> int:
    return a + b

# 调用函数
result = add(1, 2)
print(result)  # 输出：3

# 默认参数
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# 调用函数
greet("cxy")  # 输出：Hello, cxy!
greet("cxy", "Hi")  # 输出：Hi, cxy!

# 可变参数, 使用 *号，表示接收任意数量的参数
def sum_numbers(*numbers):
    print(type(numbers)) # numbers会被解析为元组 输出: <class 'tuple'>
    result = 0
    for number in numbers:
        if type(number) in (int, float):
            result += number
    return result

print(sum_numbers(1, 2))  # 输出：3
print(sum_numbers(1, 2, 3, 4))  # 输出：10

# 关键字参数
def person(name, age):
    print(f"Name: {name}, Age: {age}")

# 调用函数时, 指定参数名, 参数顺序不影响
person(age=18, name="cxy")  # 输出：Name: cxy, Age: 18

# 命名关键字参数
def person(name, *, age, gender):
    print(f"Name: {name}, Age: {age}, Gender: {gender}")

# 调用函数时, *号后面的参数，必须使用命名关键字参数
person("cxy", age=18, gender="Male")  # 输出：Name: cxy, Age: 18, Gender: Male
# person("cxy", 18, "Male")  # 输出：TypeError: person() takes 1 positional argument but 3 were given
# person("cxy", age=18, "Male")  # 输出：SyntaxError: positional argument follows keyword argument

# 参数组合
def person(name, *args, age=18, **kwargs):
    print(f"Name: {name}, Args: {args}, Age: {age}, Kwargs: {kwargs}")
# name 是必选参数，位置参数或关键字参数
# args 是可变位置参数
# age 是默认参数，仅关键字参数
# kwargs 是可变关键字参数

# 调用函数
person("cxy", "Male")  # 输出：Name: cxy, Args: ('Male',), Age: 18, Kwargs: {}
person("cxy", "Male", age=20)  # 输出：Name: cxy, Args: ('Male',), Age: 20, Kwargs: {}
person("cxy", city="chengdu")  # 输出：Name: cxy, Args: (), Age: 18, Kwargs: {'city': 'chengdu'}
person("cxy", "Male", city="chengdu", weight=60)  # 输出：Name: cxy, Args: ('Male',), Age: 18, Kwargs: {'city': 'chengdu', 'weight': 60}

# 函数参数有5种类型
# 1、POSITIONAL_ONLY 位置参数
# 2、POSITIONAL_OR_KEYWORD 位置或关键字参数
# 3、VAR_POSITIONAL 可变位置参数
# 4、KEYWORD_ONLY 仅关键字参数
# 5、VAR_KEYWORD 可变关键字参数

# 使用 inspect 库，查看函数签名，并查看参数类型
from inspect import signature

print(signature(person)) # (name, *args, age=18, **kwargs)

for name, val in signature(person).parameters.items():
    print(name, val.kind)
# name POSITIONAL_OR_KEYWORD 位置或关键字
# args VAR_POSITIONAL 可变位置
# age KEYWORD_ONLY 仅关键字
# kwargs VAR_KEYWORD 可变关键字

# 一些内置函数，只支持位置传入: ord, len, all, ...
# 我们也可以定义只支持位置传入的函数:
def posOnly(a, /):
    print(a)
posOnly(1)  # 输出：1
# posOnly(a=1)  
# 输出：TypeError: posOnly() got some positional-only arguments passed as keyword arguments: 'a'
# 也是就说，这个函数只能传位置参数，不能传关键字参数

for name, val in signature(posOnly).parameters.items():
    print(name, val.kind)
# a POSITIONAL_ONLY

# lambda 表达式
# 匿名函数，没有函数名，只能使用一次，不能重复使用
# 语法：lambda 参数: 表达式
# 返回值是一个函数
# 应用场景：当一个函数只被使用一次时，可以使用 lambda 表达式来代替

# 使用 lambda 表达式，计算两个数的和
add = lambda a, b: a + b
print(add(1, 2))  # 输出：3

# 带默认参数的 lambda 表达式
add = lambda a, b=2: a + b
print(add(1))  # 输出：3

# 带可变参数的 lambda 表达式
add = lambda *args: sum(args)
print(add(1, 2, 3, 4, 5))  # 输出：15

# lambda 表达式，可以作为返回值
def getAdd():
    return lambda a, b: a + b

add = getAdd()
print(add(1, 2))  # 输出：3

# lambda 表达式，可以作为参数传递给其他函数
def apply(func, x):
    return func(x)

print(apply(lambda x: x + 1, 1))  # 输出：2


# 函数内部使用全局变量
# 定义全局变量
globalVar = 10

def func():
    global globalVar # 表明它是全局变量, 否则下面语句报异常
    globalVar += 20
    return globalVar

print(func()) # 输出：30