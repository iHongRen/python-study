# Python 中的列表 List, 就是其他语言的中的数组 Array。
# 创建一个空列表
my_list = []

# 创建一个包含一些元素的列表
my_list = [1, 2, 3, 4, 5]

# 访问列表中的元素
print(my_list[0])  # 输出: 1
print(my_list[2])  # 输出: 3

# 获取列表中元素的索引，没有会报异常
print(my_list.index(4))  # 输出: 3

# 访问列表中的最后一个元素
print(my_list[-1])  # 输出: 5

# 访问列表中的切片
print(my_list[1:3])  # 输出: [2, 3], 从索引1到索引2的元素
print(my_list[::3])  # 输出: [1, 4], 每3步长取一个元素
print(my_list[1:4:2]) # 输出: [2, 4], 从索引1到索引3，每2步长取一个元素
print(my_list[-1:-4:-2]) # 输出: [4, 2], 从索引-1到索引-4，每2步长取一个元素

# 修改列表中的元素
my_list[0] = 10
print(my_list)  # 输出: [10, 2, 3, 4, 5]

# 获取列表的长度
print(len(my_list))  # 输出: 5

# 遍历列表
for item in my_list:
    print(item)

for index in range(len(my_list)):
    print(my_list[index])

for index, item in enumerate(my_list):
    print(index, item)
    
# 添加元素到列表末尾
my_list.append(6)
print(my_list)  # 输出: [10, 2, 3, 4, 5, 6]

# 添加元素到指定位置
my_list.insert(2, 100)  # 在索引为2的位置插入元素100
print(my_list)  # 输出: [10, 2, 100, 3, 4, 5, 6]

# 从列表中删除元素
my_list.remove(3)  # 删除元素3
print(my_list)  # 输出: [10, 2, 100, 4, 5, 6]

# 从列表中删除指定位置的元素
my_list.pop(1)  # 删除索引为1的元素
print(my_list)  # 输出: [10, 100, 4, 5, 6]

# 获取列表中元素的数量
print(my_list.count(100))  # 输出: 1

# 反转列表
my_list.reverse()
print(my_list)  # 输出: [6, 5, 4, 100, 10]

# 对列表进行排序（升序）
my_list.sort()
print(my_list)  # 输出: [4, 5, 6, 10, 100]

# 对列表进行排序（降序）
my_list.sort(reverse=True)
print(my_list)  # 输出: [100, 6, 5, 4, 10]

# 复制列表
my_list_copy = my_list.copy()
print(my_list_copy)  # 输出: [100, 6, 5, 4, 10]

my_list_copy1 = my_list[:]
print(my_list_copy1)  # 输出: [100, 6, 5, 4, 10]

# 检查元素是否在列表中
print(10 in my_list)  # 输出: True
print(20 not in my_list)  # 输出: True


# 清空列表
my_list.clear()
print(my_list)  # 输出: []


# 列表拼接
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)  # 输出: [1, 2, 3, 4, 5, 6]

# 列表比较, 对应索引位置上的元素的大小
list4 = [1, 2, 3]
print(list4 == list1)  # 输出: True
print(list4 == list2)  # 输出: False
print(list4 > list2)   # 输出: False

# 列表乘法, 重复列表
print(list1 * 3) # 输出: [1, 2, 3, 1, 2, 3, 1, 2, 3]
