# 数值类型：
#   整数(int)：1, -2
#   浮点数(float): 0.5,  3.1415926
#   复数(complex): 1j, 1+2j

# 可以使用 type() 函数查看数据类型
print(type(-2))
print(type(3.14))
print(type(1j))

# 定义变量，初始化赋值，不需要写类型
a = 1
b = 3.14
c = 1j

# 布尔类型(bool)：True, False
print(type(True))
print(a==c)


# 字符串类型(str)：
#   单引号、双引号、三引号
print(type('hello'))
h = "hello world"
print(h)

myWord = """
这是一个多行字符串，
使用三个双引号
"""
print(myWord)


# 列表类型(list)：使用方括号 [] 表示
myList = [1, 2, 3]
print(type(myList))
print(['a', 'b', 'c'])

# 元组类型(tuple)：使用圆括号 () 表示
myTuple = (1, 2, 3)
print(type(myTuple))
print(('404', 'not found'))

# 字典类型(dict)：使用大括号 {} 表示, 键值对形式
myDict = {'name': 'hongren', 'age': 18}
print(type(myDict))
print({'name': '张三', 'age': 18, 'gender': '男'})

# 集合类型(set)：也使用大括号 {} 表示
mySet = {1, 2, 3}
print(type(mySet))
print({'apple', 'banana', 'cherry'})

# 空值类型(NoneType)：None
print(type(None))


# 字节类型（bytes）：用于存储二进制数据
a = b"hello"
print(type(a))

""" 
 运算符
"""
print(100 + 200) # 加法
print(100 - 200) # 减法
print(100 * 200) # 乘法
print(100 / 200) # 除法 结果为浮点数
print(100 // 200) # 取整
print(100 % 200) # 取余
print(2 ** 10) # 求幂 2的10次方 

a = 10
b = 5.5

a += b   # 等价于 a = a + b
print(a) # 15.5 类似的 -=, *=, /=, //=, **=

# 比较
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

# 逻辑运算: and, or, not
print(a and b) # 逻辑与
print(a or b) # 逻辑或
print( not a) # 逻辑非

# 位运算: &, |, ^, ~, <<, >>
a = 10
b = 20
print(a & b) # 位与
print(a | b) # 位或
print(a ^ b) # 位异或
print(~a) # 位非
print(a << 2) # 左移
print(a >> 2) # 右移

# 成员运算: in, not in
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in 'hello')
print('a' not in 'hello')

# 身份运算: is, is not
a = [1, 2, 3]
b = [1, 2, 3]

# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
print(a is b)
print(a == b)

#  id() 函数用于获取对象内存地址
print(id(a))
print(id(b))



""" 
  类型转换
"""
a = 1
b = 6.18
c = '3.14'
d = True

print(str(a))
print(int(b)) # 转为整数,转不成功会报异常
print(float(c))
print(int(d))
print(bool(a))
print(str([1,2,3])) # 将列表转为字符串

print(chr(65)) # 将65转为转为ascii 'A',
print(ord("A")) # 将'A'转为对应的整数 65

# 一些数学函数
print(max(1, 2, 3)) # 求最大值
print(min(1, 2, 3)) # 求最小值
print(sum([1, 2, 3])) # 求和
print(abs(-10)) # 取绝对值
print(pow(2, 3)) # 2的3次方
print(round(3.1415926)) # 四舍五入
print(round(3.1415926, 2)) # 保留两位小数

import math
print(math.fabs(-10.12)) # 浮点数取绝对值
print(math.ceil(3.1415926)) # 向上取整
print(math.floor(3.1415926)) # 向下取整
print(math.sqrt(9)) # 平方根

# 随机数
import random
print(random.random()) # 0-1之间的随机浮点数
print(random.randint(0, 10)) # 0-10之间的随机整数
print(random.randrange(0, 10, 2)) # 0-10之间的随机偶数
print(random.choice('abcdefg')) # 随机选择一个字母
print(random.sample('abcdefg', 3)) # 从字符串中随机选择三个字母


# 字符串转字节
s = "apple"
a = bytes(s, encoding="utf-8")
print(a)

for i in a:
    print(i)


"""
  进制转换
"""
print(bin(10)) # 将10转为二进制
print(oct(10)) # 八进制
print(hex(10)) # 十六进制

a = bin(10)
print(int(a, 2)) # 二进制转十进制
