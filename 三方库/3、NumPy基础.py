# NumPy 基础
# pip3 install numpy

# NumPy 是 Python 中科学计算的基础库。

# 参考 https://openbiox.github.io/py4ds-CN/numpy.html

# NumPy的部分功能如下：
# ● ndarray，一个具有矢量算术运算和复杂广播能力的快速且节省空间的多维数组。
# ● 用于对整组数据进行快速运算的标准数学函数（无需编写循环）。
# ● 用于读写磁盘数据的工具以及用于操作内存映射文件的工具。
# ● 线性代数、随机数生成以及傅里叶变换功能。
# ● 用于集成由C、C++、Fortran等语言编写的代码的A C API。

# 对于大部分数据分析应用而言，功能主要集中在：
# ● 用于数据整理和清理、子集构造和过滤、转换等快速的矢量化数组运算。
# ● 常用的数组算法，如排序、唯一化、集合运算等。
# ● 高效的描述统计和数据聚合/摘要运算。
# ● 用于异构数据集的合并/连接运算的数据对齐和关系型数据运算。
# ● 将条件逻辑表述为数组表达式（而不是带有if-elif-else分支的循环）。
# ● 数据的分组运算（聚合、转换、函数应用等）。。

# NumPy之于数值计算特别重要的原因之一，是因为它可以高效处理大数组的数据。这是因为：
# ● NumPy是在一个连续的内存块中存储数据，独立于其他Python内置对象。NumPy的C语言编写的算法库可以操作内存，而不必进行类型检查或其它前期工作。比起Python的内置序列，NumPy数组使用的内存更少。
# ● NumPy可以在整个数组上执行复杂的计算，而不需要Python的for循环。

import numpy as np

# ndarray：一种多维数组对象，其中的所有元素必须是相同类型
# 每个数组都有一个shape（一个表示各维度大小的元组）和一个dtype（一个用于说明数组数据类型的对象）：

# 序列类型对象转 NumPy 数组, 以一个列表的转换为例:
arr = np.array([1, 2, 3, 4, 5])
print(arr) 
print(arr.ndim)  # 1 表示一维数组
print(arr.shape) # (5,) 表示有5个元素的一维数组
print(arr.dtype)  # int64 表示整数类型，64位

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ndim)  # 2 表示二维数组
print(arr.shape) # (2, 3) 表示有2行3列的二维数组

# 创建并用 0 填充数组
arr = np.zeros((3, 4))
print(arr)
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# 创建并用 1 填充数组
arr = np.ones((3, 4))
print(arr)
# [[1. 1. 1. 1.]
#  [1. 1. 1. 1.]
#  [1. 1. 1. 1.]]

# 创建并用特定值填充数组
arr = np.full((3, 4), 5)
print(arr)
# [[5 5 5 5]
#  [5 5 5 5]
#  [5 5 5 5]]

# 创建单位矩阵
arr = np.eye(3)
print(arr)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 创建对角矩阵
arr = np.diag([1, 2, 3, 4])
print(arr)
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]
#  [0 0 0 4]]

# 创建随机数组
arr = np.random.rand(3, 4)
print(arr)
# [[0.97354851 0.53105918 0.30133138 0.41961984]
#  [0.43242767 0.96143604 0.83402752 0.52391471]
#  [0.88781165 0.92628068 0.83673689 0.46535321]]

# 数组的索引和切片
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0, 2])  # 3, 第一个数组的第三个元素
print(arr[0][2])  # 3, 等价于上面的语句
print(arr[1, 0])  # 4, 第二个数组的第一个元素

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])  # 6, 第一个数组的第二个数组的第三个元素
print(arr[1, 0, -2])  # 8, 第二个数组的第一个数组的倒数第二个元素

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0, 1:4])  # [2 3 4], 第一个数组的第二个到第四个元素
print(arr[1, 1:4:2])  # [7 9], 第二个数组的第二个到第四个元素，步长为 2

# 数组的赋值
arr1 = arr[0, 2:4]
arr1[:] = 100  # 所有元素赋值为 100
print(arr1) # [100 100]
print(arr)
# [[  1   2 100 100   5]
#  [  6   7   8   9  10]]
# 可以看到，arr1 的值被改变了，而 arr 也发生了变化。
# 这是因为 arr1 是 arr 的一个视图，所以修改 arr1 的任何改变都会直接反映到 arr 中。

# 数组的拷贝
arr2 = arr[0, 2:4].copy() # 得到的是切片的一份副本而非视图
arr2[0] = 200
print(arr2)  # [200 100]
print(arr)  # 此时，arr的值没有发生变化
# [[  1   2 100 100   5]
#  [  6   7   8   9  10]]


# 数组的运算
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)  # [5 7 9]
print(arr1 - arr2)  # [-3 -3 -3]
print(arr1 * arr2)  # [ 4 10 18]
print(arr1 / arr2)  # [0.25 0.4 0.5]

print(arr1 * 2)  # [2 4 6]
print(arr1 / 2)  # [0.5 1.0 1.5]
print(arr1 ** 2)  # [1 4 9]
print(arr1 ** 0.5)  # [1. 1.41421356 1.73205081]

# 大小相同的数组之间的比较会生成布尔值数组
# 不同大小的数组之间的运算叫做广播（broadcasting）
print(arr1 > arr2)  # [False False False]
print(arr1 < arr2)  # [ True  True  True]
print(arr1 == arr2)  # [False False False]
print(arr1 != arr2)  # [ True  True  True]
print(arr1 >= arr2)  # [False False False]
print(arr1 <= arr2)  # [ True  True  True]

# 数组的逻辑运算
arr1 = np.array([True, False, True])
arr2 = np.array([False, False, True])
print(np.logical_and(arr1, arr2))  # [False  False  True]
print(np.logical_or(arr1, arr2))  # [ True False  True]
print(np.logical_not(arr1))  # [False  True False]


# 数组的转置和轴对换
# reshape 改变数组形状
arr = np.arange(9).reshape(3, 3)
print(arr)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

# T属性，转置
print(arr.T) # 等价于 arr.transpose()
# [[0 3 6]
#  [1 4 7]
#  [2 5 8]]

# 轴对换
print(arr.swapaxes(1, 0)) 
# [[0 3 6]
#  [1 4 7]
#  [2 5 8]]

# 迭代
# 对多维数组进行 迭代（Iterating） 是相对于第一个轴完成的：
for x in arr:
    print(x)
# [0 1 2]
# [3 4 5]
# [6 7 8]

# 对数组中的每个元素执行操作，可以使用flat属性
for x in arr.flat:
    print(x, end='')
# 012345678

# 通用函数 ufunc
# 通用函数是一组用于对数组中的元素进行计算的函数
arr = np.arange(5) # [0 1 2 3 4]
print(np.sqrt(arr))  # 开根号
# [0.         1.         1.41421356 1.73205081 2.        ]

print(np.power(arr, 3)) # 幂运算
# [ 0  1  8 27 64]





