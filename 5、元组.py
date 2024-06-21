# 元组(tuple)与列表类似, 也是一组数据, 但元组一旦初始化就不能修改。
# 也就是说你不能向元组中添加、删除、修改元素。
# 元组使用小括号来表示, 元素之间用逗号分隔。

# 创建一个空元组
my_tuple = ()
print(type(my_tuple))  # 输出: <class 'tuple'>

# 创建一个元素的元组，
# 需要在元素后添加一个逗号，否则会被识别为一个带括号的变量
my_tuple = (1,)
my_tuple = (1) # 错误写法，这不是一个元组，而是一个整数


# 创建一个包含多个元素的元组
my_tuple = ('cxy', 18, 'male')
print(my_tuple)  # 输出: ('cxy', 18, 'male')

# 使用索引来访问元组中的元素, 
print(my_tuple[0])  # 输出: cxy
print(my_tuple[1])  # 输出: 18

# 使用切片来访问元组中的元素, 
# 注意: 切片的结果仍然是一个元组
print(my_tuple[1:3])  # 输出: (18, 'male')
print(my_tuple[:2])  # 输出: ('cxy', 18)

# 判断元素是否在元组中
print('cxy' in my_tuple)  # 输出: True
print('female' not in my_tuple)  # 输出: True

# 不可变性
# 修改元组中的元素（报错）
# my_tuple[0] = 'cxy1'  # 修改元组中的元素（报错）
# del my_tuple[0]  # 元组中的元素（报错）

# 获取元组的长度
print(len(my_tuple))  # 输出: 3

# 遍历元组
for item in my_tuple:
    print(item)

for index in range(len(my_tuple)):
    print(my_tuple[index])

for index, value in enumerate(my_tuple):
    print(index, value)

# 解包元组
a, b, c = my_tuple
print(a, b, c)  # 输出: cxy 18 male
# *号表达式
x, *y = my_tuple
print(x, y)  # 输出: cxy [18, 'male']

# 交换两个变量的值
a, b = 1, 2
a, b = b, a
print(a, b)

# 连接元组
my_tuple1 = (1, 2, 3)
my_tuple2 = (4, 5, 6)
my_tuple3 = my_tuple1 + my_tuple2
print(my_tuple3)  # 输出: (1, 2, 3, 4, 5, 6)

# 复制元组
my_tuple4 = my_tuple3
print(my_tuple4)  # 输出: (1, 2, 3, 4, 5, 6)

# 列表转元组
my_list = [1, 2, 3]
my_tuple5 = tuple(my_list)
print(my_tuple5)  # 输出: (1, 2, 3)

# 元组转列表
my_tuple6 = (1, 2, 3)
my_list2 = list(my_tuple6)
print(my_list2)  # 输出: [1, 2, 3]

# 获取元组中的最大值和最小值
my_tuple7 = (1, 2, 3, 4, 5)
max_value = max(my_tuple7)
min_value = min(my_tuple7)
print(max_value, min_value)  # 输出: 5 1

# 统计元组中某个元素出现的次数
my_tuple8 = (1, 2, 3, 4, 5, 1, 2, 3)
count = my_tuple8.count(1)
print(count)  # 输出: 2

# 命名元组, 可以通过字段名来获取属性值
from collections import namedtuple

# 创建一个命名元组
Person = namedtuple('Person', ['name', 'age', 'gender'])
person1 = Person('cxy', 18, 'male')
print(person1)  # 输出: Person(name='cxy', age=18, gender='male')

# 访问命名元组的属性
print(person1.name)  # 输出: cxy
print(person1.age)  # 输出: 18
print(person1.gender)  # 输出: male


# 元组和列表 
# 列表是可变数据类型，元组是不可变数据类型
# 列表比元组更占内存
# 创建列表也比创建元组更耗时
import sys
import timeit

a = list(range(100000))
b = tuple(range(100000))
print(sys.getsizeof(a), sys.getsizeof(b)) # 输出: 800056 800040  

print(timeit.timeit('[1, 2, 3, 4, 5, 6, 7, 8, 9]'))
print(timeit.timeit('(1, 2, 3, 4, 5, 6, 7, 8, 9)'))
# 输出:
# 0.11076129200228024
# 0.011807375001808396
