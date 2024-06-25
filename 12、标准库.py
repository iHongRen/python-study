# 标准库

# Python 内置了很多有用的模块，我们可以直接使用。比如:

import os # 多种操作系统接口
import io # 文件和流操作
import sys  # 系统相关操作
import math  # 数学运算
import json  # 处理 JSON 数据
import re  # 正则表达式
import requests  # 网络请求
import random  # 随机数生成
import string  # 字符串操作
import hashlib  # 哈希算法
import base64  # 编码和解码 Base64 数据
import time  # 时间相关操作
import datetime  # 更高级的日期和时间操作
import uuid  # 生成唯一标识符


# os 模块提供了与操作系统相关的功能。
# 获取当前工作目录
print(os.getcwd())

# 获取当前目录文件列表
print(os.listdir('.'))


# io 模块提供了与文件和流相关的功能。
# 读取文件内容
with io.open('my_module.py', 'r') as f:
    content = f.read()
    print(content)

# math 模块提供了数学运算相关的功能。
print(math.sqrt(16)) # 计算平方根, 输出: 4
print(math.pow(2, 3)) # 计算2的3次方, 输出: 8
print(math.floor(3.7)) # 向下取整, 输出: 3

# random 模块提供了随机数生成相关的功能。
print(random.randint(1, 10)) # 生成1到10之间的随机整数
print(random.random()) # 生成0到1之间的随机浮点数
print(random.choice(['apple', 'banana', 'cherry'])) # 从列表中随机选择一个元素
print(random.sample(['apple', 'banana', 'cherry'], 2)) # 从列表中随机选择两个元素

# hashlib 模块提供了哈希算法相关的功能。
# 计算MD5哈希值
hash_object = hashlib.md5(b'hello world')
print(hash_object.hexdigest()) # 输出: 5eb63bbbe01eeed093cb22bb8f5acdc3

# 计算SHA1哈希值
hash_object = hashlib.sha1(b'hello world')
print(hash_object.hexdigest()) # 输出: 2aae6c35c94fcfb415dbe95f408b9ce91ee846ed


# base64 模块提供了编码和解码 Base64 数据的功能。
# 编码Base64数据
base64_data = base64.b64encode(b'hello world').decode('utf-8')
print(base64_data) # 输出: aGVsbG8gd29ybGQ=

# 解码Base64数据
decode_data = base64.b64decode(base64_data).decode('utf-8')
print(decode_data) # 输出: hello world


# uuid 模块提供了生成唯一标识符的功能。
# uuid1 由MAC地址、当前时间戳、随机数生成，可以保证全球范围内的唯一性。
print(uuid.uuid1().hex) 

# uuid3 通过计算命名空间和名字的MD5哈希摘要（“指纹”）值得到，保证了同一命名空间中不同名字的唯一性，和不同命名空间的唯一性，但同一命名空间的同一名字会生成相同的UUID。
print(uuid.uuid3(uuid.NAMESPACE_DNS, 'cxy').hex) 

# uuid4 由伪随机数生成UUID，有一定的重复概率，该概率可以计算出来。
print(uuid.uuid4().hex) 

# uuid5 算法与uuid3相同，只不过哈希函数用SHA-1取代了MD5。
print(uuid.uuid5(uuid.NAMESPACE_DNS, 'cxy').hex) 

# 参考 https://github.com/jackfrued/Python-Core-50-Courses/blob/master/%E7%AC%AC20%E8%AF%BE%EF%BC%9APython%E6%A0%87%E5%87%86%E5%BA%93%E5%88%9D%E6%8E%A2.md