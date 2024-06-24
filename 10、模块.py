# 模块 Module

# 模块是 Python 中一个独立的 .py文件，可以包含函数、类、变量等，可以被其他文件导入使用。
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突
# 模块名应该尽量简单，不要使用太长的模块名
# 模块名应该尽量使用单数形式，不要使用复数形式
# 模块名应该尽量使用小写字母，不要使用大写字母
# 模块名应该尽量使用下划线连接各个单词


# 导入模块的几种方式：

# 1、标准导入
# 导入 my_module 模块
import my_module

# 使用模块中的变量和函数
print(my_module.PI)  # 输出: 3.14159
print(my_module.add(2, 3))  # 输出: 5
print(my_module.subtract(5, 3))  # 输出: 2


# 2、选择性导入 
# 仅导入 my_module 中的 add 和 PI
from my_module import add, PI

# 使用导入的对象
print(PI)  # 输出: 3.14159
print(add(2, 3))  # 输出: 5

# 3、带别名的导入
# 导入 my_module 模块，并给它取个别名
import my_module as mm

# 使用别名
print(mm.PI)  # 输出: 3.14159
print(mm.add(2, 3))  # 输出: 5
print(mm.subtract(5, 3))  # 输出: 2

# 4、带别名的选择性导入
from my_module import add as add_func, PI as pi
print(add_func(2, 3))  # 输出: 5
print(pi)  # 输出: 3.14159

# 5、通配符导入
# 导入 my_module 模块中的所有对象
# 不建议从模块或包内导入 *, 
# 因为这样可能会导入一些不需要的对象，甚至覆盖已经定义的名称，导致代码难以维护
from my_module import *
my_function()

# 6、相对导入
# 如果您需要导入同一个包内部的模块,可以使用相对导入的方式。
# from . import my_module  # 导入当前目录下的 my_module 模块
# from .. import my_module  # 导入上一级目录下的 my_module 模块
