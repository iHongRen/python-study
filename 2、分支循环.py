# if 语句，和其他语言不同，没有小括号，大括号。但有冒号:
x = 1
if x > 0:
    print('x 大于 0')


# if-else 语句
x = -1
if x > 0:
    print('x 大于 0')
else:
    print('x 小于或等于 0')

# if-elif-else 语句
x = 0
if x > 0:
    print('x 大于 0')
elif x == 0:
    print('x 等于 0')
else:
    print('x 小于 0')


# match-case 语句，Python 3.10 加入
# 就是其他语言的 switch-case 语句。
# case _: 表示默认，与其他语言 default: 一样
x = 2
match x:
    case 0:
        print('x 等于 0')
    case 1:
        print('x 等于 1')
    case _:
        print('x 不等于 0，也不等于 1')


# for-in 循环
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)

# for-in...else 循环, 结束后会执行 else 子句
for i in arr:
    print(i)
else:
    print('循环结束')

# 在循环中遇到 break 语句，则会中断循环，此时不会执行 else 子句。
for i in arr:
    if i == 3:
        break
    print(i)
else:
    print('循环结束')


# while 循环
x = 0
while x < 5:
    print(x)
    x += 1

# while...else 循环, 结束后会执行 else 子句，同样遇到 break 后，不会执行 else。
x = 0
while x < 5:
    print(x)
    x += 1
    if x == 3:
        break
else:
    print('循环结束')

# continue 语句，跳过本次循环，继续下一次循环
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)


# pass 是空语句，是为了保持程序结构的完整性
# 什么也不做，一般用于占位，避免出现语法错误
x = 1
if x > 0:
    pass
else:
    print("x 是负数")

# 空类，什么也不做，
# 空类可以用于继承，但不能实例化
class EmptyClass:
    pass

# 空函数，什么也不做，
def empty_function():
    pass


# range 函数, 生成一个序列
# 遍历 0 - 4
for i in range(5):
    print(i)

# 遍历 1 - 5
for i in range(1, 6):
    print(i)
1

# 遍历 0 - 9， 步长为 2
for i in range(0, 10, 2):
    print(i)
# 0 2 4 6 8
