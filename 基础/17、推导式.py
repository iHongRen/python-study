# 推导式

# 推导式是一种简洁的数据结构形式，可以从一个数据序列生成另一个数据序列。


# 基本语法如下：
# new_list = [表达式 for 变量 in 可迭代对象 if 条件]

# 常用的推导式有以下几种：
# - 列表推导式
# - 字典推导式
# - 集合推导式
# - 元组推导式


############# 列表推导式
# 例子1：对列表中的元素求平方，得到新列表
numbers = [1, 2, 3]

# 直接使用 for-in 循环
squares = []
for number in numbers:
    squares.append(number ** 2)
print(squares) # 输出: [1, 4, 9]

# 使用推导式
squares = [number ** 2 for number in numbers]
print(squares) # 输出: [1, 4, 9]

# 使用 map
squares = list(map(lambda x: x ** 2, numbers))
print(squares) # 输出: [1, 4, 9]


# 例子2：筛选出列表中的偶数，得到新列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 直接使用 for-in 循环
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(evens) # 输出: [2, 4, 6, 8, 10]

# 使用推导式
evens = [number for number in numbers if number % 2 == 0]
print(evens) # 输出: [2, 4, 6, 8, 10]

# 使用 filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # 输出: [2, 4, 6, 8, 10]


############# 字典推导式
# 例子1：对字典中key*2, value*2，得到新字典
d = {'x': 1, 'y': 2, 'z': 3}

# 直接使用 for-in 循环
new_d = {}
for key in d:
    new_d[key*2] = d[key] * 2
print(new_d) # 输出: {'xx': 2, 'yy': 4, 'zz': 6}

# 使用推导式
new_d = {key*2: d[key] * 2 for key in d}
print(new_d) # 输出: {'xx': 2, 'yy': 4, 'zz': 6}


# 使用 map
new_d = dict(map(lambda x: (x[0]*2, x[1] * 2), d.items()))
print(new_d) # 输出: {'xx': 2, 'yy': 4, 'zz': 6}

# 例子2：过滤掉key=z，得到新字典

# 直接使用 for-in 循环
new_d = {}
for key in d:
    if key != 'z':
        new_d[key] = d[key]
print(new_d) # 输出: {'x': 1, 'y': 2}

# 使用推导式
new_d = {key: value for key, value in d.items() if key != 'z'}
print(new_d) # 输出: {'x': 1, 'y': 2}

# 使用 filter
new_d = dict(filter(lambda x: x[0] != 'z', d.items()))
print(new_d) # 输出: {'x': 1, 'y': 2}


# 例子3：将字典 d 的值进行平方，并组成为一个列表
new_list = [x ** 2 for x in d.values()]
print(new_list) # 输出: [1, 4, 9]



############# 元组推导式
# 例子1：对元组中的元素求平方，得到新元组
numbers = (1, 2, 3)

# 使用推导式
t = (number ** 2 for number in numbers)
print(t) # 返回一个生成器，<generator object <genexpr> at 0x10aa17920>

# 使用 tuple() 转换成元组
print(tuple(t)) # 输出: (1, 4, 9)

