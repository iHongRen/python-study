# 来自 110道Python面试题

# 1、 一行代码实现1-100之和
print(sum(range(1, 101)))

# 2、如何在一个函数内部修改全局变量
globalVar = 100
def modifyGlobalVar():
    global globalVar # 主要靠global关键字
    globalVar = 200

modifyGlobalVar()
print(globalVar)

# 3、列出5个python标准库
import sys # 系统相关
import os # 操作系统相关
import shutil # 文件相关
import re # 正则表达式
import math # 数学相关

# 4、字典如何删除键和合并两个字典
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict1.update(dict2)
print(dict1)

dict1.pop('b')
print(dict1)

# 5、谈一下python的GIL
"""
GIL全名为全局解释器锁（Global Interpreter Lock）。这是一种线程管理机制，并不根属于Python语言，而是存在于CPython中。
在GIL锁开启的情况下，同个进程内的多个线程只能串行而不能并行。
GIL的释放有两种触发方式，一种是遇到I/O操作，另一种则是超出时间限制。
遇到I/O操作时，原线程运行结束，其余线程对CPU使用权进行「竞争」。
但如果是超时释放，原来运行的线程会重新加入这场「竞争」。
这种做法是出于安全性考虑，但已经不能适应时代的发展。
根据GIL的原理，对主要进行I/O操作的程序，比如网页爬虫，受到的影响并不大。
而对于计算密集型的程序来说，就是另一回事了。
GIL诞生时的CPU还只有一个核心，但在发展的过程中，GIL始终保持着全局锁定的特性。
这就导致了在多核CPU早已普及的今天，多出的核心并没有被利用，大量算力被浪费。
这意味着，对于AI、ML等计算密集领域，效率会出现严重降低。
AI发展如火如荼的现在，姗姗来迟的解决方案终于出炉。
Python官方宣布，在新版的CPython中，GIL锁将成为「可选择项」。
"""


# 6、python实现列表去重的方法
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list1 = list(set(list1))
print(list1)

# 7、fun(*args, **kwargs) 中的*args和**kwargs什么意思
# *args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。
# 并且同时使用*args和**kwargs时，必须*args参数列要在**kwargs前


# 8、一句话解释什么样的语言能够用装饰器
# 函数可以作为参数传递的语言，可以使用装饰器


# 9、简述面向对象中__new__和__init__方法的区别
# __new__在对象实例化的时候调用，该方法有一个参数cls，指代的是当前类，它有返回值，返回实例化出来的实例。 
# __init__在对象初始化的时候调用，该方法有一个参数self，指代的实例对象本身，该方法不能有返回值，用于初始化参数；
class MyClass:
    def __new__(cls, *args, **kwargs):
        print("new")
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print("init")
        super().__init__()

myInst = MyClass()
print(myInst)


# 10、字符串 a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"
import re
a = "not 404 found 张三 99 深圳"
res = re.sub(r'[a-zA-Z0-9]', '', a).strip().replace('  ', ' ')
print(res)

# 11、如何在python中实现单例模式
# 用__new__方法实现
class SingletonNew(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

print(SingletonNew())
print(SingletonNew())

# 用__call__方法实现
class SingletonCall(object):
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__call__(*args, **kwargs)
        return cls.instance
    
print(SingletonCall())
print(SingletonCall())

# 用装饰器实现
def singleton(cls):
    instance = {}
    def wrapper(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper

@singleton
class MySingleton(object):
    def __init__(self, name):
        self.name = name

print(MySingleton('张三').name)
print(MySingleton('李四').name)





