# 统计指定目录代码行数

import os
import time

def useTime(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        ret = func(*args, **kwargs)
        endTime = time.time()
        print ('总耗时: %0.2fs' % (endTime - startTime))
        return ret
    return wrapper

def fileLines(filePath):
    count = 0
    with open(filePath, 'rb') as f:
        lines = f.readlines()
        for line in lines:
            if len(line.strip()) != 0: #过滤掉空行
                count += 1
    print (f'{filePath} --------: {count}')
    return count

@useTime
#遍历文件, 递归遍历文件夹中的所有
def calcCodeLines(dir, fileExts):
    lines = 0
    for parent,dirnames,filenames in os.walk(dir):
        for filename in filenames:
            ext = filename.split('.')[-1]
            #只统计指定的文件类型
            if ext in fileExts:
                filePath = os.path.join(parent, filename)
                lines += fileLines(filePath)
    return lines

#统计一个的行数
if __name__ == '__main__' :
    # 计算当前目录, py文件的代码总行数
    totalLine = calcCodeLines('./', fileExts=['py'])
    print (f'总行数: {totalLine}')
