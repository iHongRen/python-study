# 和其他语言的字典差异不大
# 使用{}表示，键值对用冒号:分割

# 空字典
my_dict = {}
print(type(my_dict))  # 输出：<class 'dict'>

# 创建字典
my_dict = {'name': 'cxy', 'age': 20, 'gender': 'male'}

# 访问字典中的值
print(my_dict['name'])  # 输出：cxy
# print(my_dict['name1'])  # 访问不到报异常 输出：KeyError: 'name1'
print(my_dict.get('name1')) # 访问不到返回 None,
print(my_dict.get('name1', 'default')) # 访问不到返回默认值 default

print(my_dict.keys) # 输出：dict_keys(['name', 'age', 'gender'])
print(my_dict.values) # 输出：dict_values(['cxy', 20, 'male'])
print(my_dict.items) # 输出：dict_items([('name', 'cxy'), ('age', 20), ('gender', 'male')])

# 判断键是否存在
if 'name' in my_dict:
    print('存在')
else:
    print('不存在')

# 元素个数
print(len(my_dict))  # 输出：3

# 判断字典是否为空
print(my_dict == {})  # 输出：False

# 复制字典，浅复制
my_dict1 = my_dict.copy()
print(my_dict1)  # 输出：{'name': 'cxy', 'age': 20, 'gender': 'male'}

# 合并字典
my_dict2 = {'weight': 60}
my_dict2.update(my_dict1)
print(my_dict2)  # 输出：{'weight': 60, 'name': 'cxy', 'age': 20, 'gender': 'male'}

# 遍历
for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

# 添加元素
my_dict['address'] = '成都'
print(my_dict)  # 输出：{'name': 'cxy', 'age': 20, 'gender': 'male', 'address': '成都'}

# 修改元素
my_dict['age'] = 21 
my_dict.update({'name': 'cxy1', 'age': 22})
print(my_dict)  # 输出：{'name': 'cxy1', 'age': 22, 'gender': 'male', 'address': '成都'}

my_dict.update(age=19, gender='男') 
print(my_dict)  # 输出：{'name': 'cxy1', 'age': 19, 'gender': '男', 'address': '成都'}

# 存在name就修改为李四，
# 不存在name就添加 name: '李四'
my_dict.setdefault('name', '李四')
print(my_dict)

# 删除元素
del my_dict['address']
print(my_dict)  # 输出：{'name': 'cxy1', 'age': 19, 'gender': '男'}

# 也是删除元素
my_dict.pop('gender')
print(my_dict)  # 输出：{'name': 'cxy1', 'age': 19}

# 删除最后一个元素
key, value = my_dict.popitem()
print(key, value)
print(my_dict)  # 输出：{'name': 'cxy1'}

# 清空字典  
my_dict.clear()
print(my_dict)  # 输出：{}