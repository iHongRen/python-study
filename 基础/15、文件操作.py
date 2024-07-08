# 文件操作

# Python 通过 C 函数访问系统调佣，进行文件读写。

# 打开文件
# 文件打开模式 mode
# r 以只读方式打开文件，不存在报错 FileNotFoundError
# w 以只写方式打开文件，如果该文件已存在，则覆盖原内容；不存在，则先创建文件
# x 以只写方式打开文件，如果该文件已存在，则报错 FileExistsError
# a 以追加方式打开文件，文件不存在，则先创建文件
# + 以更新（可读可写）方式打开文件，与其他模式组合使用，如 'r+'

# 数据流在读写时又分为两种转换模式:
# 't' 文本模式(默认)，'r' == 'rt'
# 'b' 二进制模式，不需要指定编码

# 以只读文本模式打开文件，指定编码为 utf-8
f = open('14、网络.py', mode='r', encoding='utf-8')
print(f.name, f.mode, f.encoding, f.closed) # 输出: 14、网络.py r utf-8 False
f.close() # 关闭文件

# 使用 with 语句打开文件，会自动关闭文件
with open('14、网络.py', mode='r', encoding='utf-8') as f:
    # 从光标位置开始，读取5个字符
    print(f.read(5)) # 输出: # 网络

    # 返回光标位置
    print(f.tell()) # 输出: 5

    # 设置光标位置
    f.seek(0) # 从头开始

    # print(f.read()) # 读取全部内容
    # print(f.readline()) # 读取一行
    # print(f.readlines()) # 读取所有行

# 以只读二进制模式打开文件
with open('14、网络.py', mode='rb') as f:
    # 从光标位置开始，读取5个字节，而不是字符。
    print(f.read(5)) # 输出: b'# \xe7\xbd\x91'
    
### 任何对文件的读取和写入动作，都会自动改变文件的光标偏移位置。


# 写入文件
# 以只写模式打开文件，指定编码为 utf-8
with open('hello.txt', mode='w', encoding='utf-8') as f:
    f.write('你好，世界！')


import json

# 写入 JSON 数据
with open('data.json', mode='w', encoding='utf-8') as f:
    data = {'name': '小明', 'age': 18}
    json.dump(data, f, ensure_ascii=False)

# 读取 JSON 数据
with open('data.json', mode='r', encoding='utf-8') as f:
    data = json.load(f)
    print(data) # 输出: {'name': '小明', 'age': 18}


# 使用 os 模块操作文件和目录
import os
import shutil

# 获取当前工作目录
print(os.getcwd())

# 创建/删除文件
filename = '自定义文件'
with open(filename, mode='w') as f:
    pass

os.remove(filename)
# os.unlink(filename) # 文件不存在会报错

# 创建/删除目录
dirname = '自定义目录'
mutilDir = '多级目录/子目录'
os.mkdir(dirname)
os.makedirs(mutilDir)

os.rmdir(dirname)
os.removedirs(mutilDir) # 递归删除

# 重命名文件
os.rename('hello.txt', 'hello1.txt')

# 获取文件元数据
d = os.stat('14、网络.py')
print(d.st_size) # 文件大小
print(d.st_atime) # 最后访问时间
print(d.st_mtime) # 最后修改时间
print(d.st_ctime) # 创建时间

# 获取文件大小
print(os.path.getsize('14、网络.py'))

# 使用 os.walk()遍历，获取文件夹内容大小
def get_folder_size(path):
    total_size = 0
    for item in os.walk(path):
        for file in item[2]:
            try:
                total_size += os.path.getsize(os.path.join(item[0], file))
            except Exception as e:
                print("error with file:  " + os.path.join(item[0], file))
    return total_size

print(get_folder_size('.'))

# 判断文件是否存在
print(os.path.exists('14、网络.py'))

# 复制文件
shutil.copy('14、网络.py', '14、网络-备份.py')

# 移动文件
shutil.move('hello1.txt', 'hello2.txt')


## 参考 https://pythonhowto.readthedocs.io/zh-cn/latest/file.html