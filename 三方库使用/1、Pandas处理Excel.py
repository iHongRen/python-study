# 使用 Pandas 库处理 Excel 文件

# Pandas 是一个强大的分析结构化数据的工具集；它的使用基础是 Numpy（提供高性能的矩阵运算）；
# 用于数据挖掘和数据分析，同时也提供数据清洗功能。

import pandas as pd

# 1、生成 Excel 文件
data = {
    "姓名": ["张三", "李四", "王五"],
    "性别": ["男", "女", "男"],
    "年龄": [18, 19, 20],
}
df = pd.DataFrame(data)
df.to_excel("student.xlsx", index=False)



# 2、读取 Excel 文件
# sheet_name 为工作表名,默认为 0,即第一个。也可以直接写表名: 'Sheet1'
# 也可以是数组 ['Sheet1','Sheet2']，读取多个表
df = pd.read_excel("student.xlsx", sheet_name=0)
print(df)
#    姓名 性别  年龄
# 0  张三  男  18
# 1  李四  女  19
# 2  王五  男  20



# 3、查看大小
print(df.shape) # (3, 3)



# 4、读取数据
# 读取行索引
print(df.index.values) # [0 1 2]

# 读取列名
print(df.columns.values) # ['姓名' '性别' '年龄']

# 读取指定列的数据
print(df['姓名'].values) # ['张三', '李四', '王五']

# iloc 方法，读取指定行列索引的数据
print(df.iloc[0].values) # ['张三' '男' '18']

# 读取前两行数据
print(df.iloc[0:2].values)
# [['张三' '男' 18]
#  ['李四' '女' 19]]

# 读取第二行第三列数据
print(df.iloc[1, 2]) # 19 ，下标从 0 开始，所以 1 表示第二行，2 表示第三列


# loc 方法，读取指定行列名的数据
print(df.loc[0, '姓名']) # 张三

# 读取第二行到第三行，姓名和年龄两列数据
print(df.loc[1:2, ['姓名','年龄']])
#    姓名  年龄
# 1  李四  19
# 2  王五  20


# 查找年龄大于 18 的数据
conf = df['年龄'] > 18
print(df[conf])
# 或者 print(df.loc[conf])
#    姓名 性别  年龄
# 1  李四  女  19
# 2  王五  男  20

# 查找性别为 男 的数据
conf = df['性别'] == '男'
print(df[conf])
# 或者 print(df.loc[conf])
#    姓名 性别  年龄
# 0  张三  男  18
# 2  王五  男  20


# 5、增加数据
# 增加一行数据
df.loc[3] = ['赵六', '女', 21]
print(df)
#    姓名 性别  年龄
# 0  张三  男  18
# 1  李四  女  19
# 2  王五  男  20
# 3  赵六  女  21

# 增加一列数据
df['班级'] = ['一班', '二班', '三班', '四班']
print(df)
#    姓名 性别  年龄  班级
# 0  张三  男  18  一班
# 1  李四  女  19  二班
# 2  王五  男  20  三班
# 3  赵六  女  21  四班


# 6、修改数据
# 修改第二行数据
df.iloc[1] = ['李4', '男', 22, '二班']
print(df)
#    姓名 性别  年龄  班级
# 0  张三  男  18  一班
# 1  李4  男  22  二班
# 2  王五  男  20  三班
# 3  赵六  女  21  四班


# 修改 王五 年龄为 21
conf = df['姓名'] == '王五'
df.loc[conf, '年龄'] = 21
print(df[conf]) # 只打印 王五 的数据
#    姓名 性别  年龄  班级
# 2  王五  男  21  三班


# 7、删除数据
# 删除 王五 的数据, 先找到行索引，再用 drop 删除
index = df[df['姓名'] == '王五'].index
df = df.drop(index)

# 或者直接过滤
# df = df[df['姓名'] != '王五']

print(df)
#    姓名 性别  年龄  班级
# 0  张三  男  18  一班
# 1  李4  男  22  二班
# 3  赵六  女  21  四班

# 再次写入
df.to_excel("student1.xlsx", index=False)
