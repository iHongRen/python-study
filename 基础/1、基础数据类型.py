# 数值类型：
#   整数(int)：1, -2
#   浮点数(float): 0.5,  3.1415926
#   复数(complex): 1j, 1+2j

# 可以使用 type() 函数查看数据类型
print(type(-2)) # 输出:<class 'int'>
print(type(3.14)) # 输出:<class 'float'>
print(type(1j)) # 输出:<class 'complex'>

# 定义变量，初始化赋值，不需要写类型
a = 1
b = 3.14
c = 1j

# 布尔类型(bool)：True, False
print(type(True)) # 输出: <class 'bool'>
print(a==c) # 输出: False


# 字符串类型(str)：
#   单引号、双引号、三引号
print(type('hello')) # 输出: <class 'str'>
h = "hello world"
print(h)

myWord = """
这是一个多行字符串，
使用三个双引号
"""
print(myWord)


# 列表类型(list)：使用方括号 [] 表示
myList = [1, 2, 3]
print(type(myList)) # 输出: <class 'list'>
print(['a', 'b', 'c'])

# 元组类型(tuple)：使用圆括号 () 表示
myTuple = (1, 2, 3)
print(type(myTuple)) # 输出: <class 'tuple'>
print(('404', 'not found'))

# 字典类型(dict)：使用大括号 {} 表示, 键值对形式
myDict = {'name': 'hongren', 'age': 18}
print(type(myDict)) # 输出: <class 'dict'>
print({'name': '张三', 'age': 18, 'gender': '男'})

# 集合类型(set)：也使用大括号 {} 表示
mySet = {1, 2, 3}
print(type(mySet)) # 输出: <class 'set'>
print({'apple', 'banana', 'cherry'})

# 空值类型(NoneType)：None
print(type(None)) # 输出: <class 'NoneType'>


# 字节类型（bytes）：用于存储二进制数据
a = b"hello"
print(type(a)) # 输出: <class 'bytes'>

""" 
 运算符
"""
print(100 + 200) # 加法, 输出: 300
print(100 - 200) # 减法, 输出: -100
print(100 * 200) # 乘法, 输出: 20000
print(100 / 200) # 除法 结果为浮点数, 输出: 0.5
print(100 // 200) # 取整, 输出: 0
print(100 % 200) # 取余, 输出: 100
print(2 ** 10) # 求幂 2的10次方, 输出: 1024

a = 10
b = 5.5

a += b   # 等价于 a = a + b, 类似的还有 -=, *=, /=, //=, **=
print(a) # 输出: 15.5 

# 比较
print(a==b) # 输出: False
print(a!=b) # 输出: True
print(a>b) # 输出: True
print(a<b) # 输出: False
print(a>=b) # 输出: True
print(a<=b) # 输出: False

# 逻辑运算: and, or, not
print(a>10 and b>10) # 逻辑与, 输出: False
print(a>10 or b>10) # 逻辑或, 输出: True
print(not a>10) # 逻辑非, 输出: False

# 位运算: &, |, ^, ~, <<, >>
a = 1
b = 0
print(a & b) # 位与, 输出: 0
print(a | b) # 位或, 输出: 1
print(a ^ b) # 位异或, 输出: 1
print(~a) # 位非, 等价于 -(a + 1), 输出: -2
print(a << 3) # 左移, 等价于a * 2的3次方, 输出: 8
print(a >> 3) # 右移, 等价于a / 2的3次方, 输出: 0

# 成员运算: in, not in
print(1 in [1, 2, 3]) # 输出: True
print(1 not in [1, 2, 3]) # 输出: False
print('a' in 'hello') # 输出: False
print('a' not in 'hello') # 输出: True

# 身份运算: is, is not
# is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # 输出: False
print(a == b) # 输出: True

#  id() 函数用于获取对象内存地址
print(id(a)) # 输出: 4506456128 (每次打印的值都不一样)
print(id(b)) # 输出: 4506758656



""" 
  类型转换
"""
a = 1
b = 6.18
c = '3.14'
d = True

print(str(a)) # 输出: '1'
print(int(b)) # 输出: 6,转不成功会报异常
print(float(c)) # 输出: 3.14
print(int(d)) # 输出: 1
print(bool(a)) # 输出: True
print(str([1,2,3])) # 输出: '[1,2,3]'

print(chr(65)) # 将65转为转为ascii 'A',
print(ord("A")) # 将'A'转为对应的整数 65

# 一些数学函数
print(max(1, 2, 3)) # 求最大值, 输出: 3
print(min(1, 2, 3)) # 求最小值, 输出: 1
print(sum([1, 2, 3])) # 求和, 输出: 6
print(abs(-10)) # 取绝对值, 输出: 10
print(pow(2, 3)) # 2的3次方, 输出: 8
print(round(3.1415926)) # 四舍五入, 输出: 3
print(round(3.1415926, 2)) # 保留两位小数, 输出: 3.14

import math
print(math.fabs(-10.12)) # 浮点数取绝对值, 输出: 10.12
print(math.ceil(3.1415926)) # 向上取整, 输出: 4
print(math.floor(3.1415926)) # 向下取整, 输出: 3
print(math.sqrt(9)) # 平方根, 输出: 3.0

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
print(a) # 输出: b'apple'

for i in a:
    print(i)


"""
  进制转换
"""
print(bin(10)) # 将10转为二进制, 输出: 0b1010
print(oct(10)) # 八进制, 输出: 0o12
print(hex(10)) # 十六进制, 输出: 0xa

a = bin(10)
print(int(a, 2)) # 二进制转十进制, 输出: 10
