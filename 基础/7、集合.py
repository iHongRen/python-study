# 集合 set 

# set 对象是由具有唯一性的 hashable(可哈希) 对象所组成的无序多项集。
# 常用来做成员检测、去重、以及数学中的集合计算(交集、差集...)
# 使用{}表示，元素用逗号分隔，
# 集合中的元素必须是不可变类型，
# 集合中的元素是可哈希的，
# 集合中的元素是无序的，
# 集合中的元素不能重复。

# 空集合,得用set()
s = set()
d = {} # 字典
print(s, type(s)) # 输出: set() <class 'set'>
print(d, type(d)) # 输出: {} <class 'dict'>


# 集合的创建
# 使用set()函数
s = set('abc') # 会将字符分割
print(s) # 输出: {'a', 'b', 'c'} 

# 使用{}
s = {'abc'}  
print(s) # 输出: {'abc'} 

s = {'a', 'b', 'c'}
print(s) # 输出: {'a', 'b', 'c'} 

# 集合操作
s.add('d')
print(s) # 输出: {'a', 'b', 'c', 'd'} 

s.update('ef')
print(s) # 输出: {'a', 'b', 'c', 'd', 'e', 'f'} 

s.update(['g', 'h'])
print(s) # 输出: {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}

# 删除元素，如果元素不存在会引发KeyError
s.remove('a')
print(s) # 输出: {'b', 'c', 'd', 'e', 'f', 'g', 'h'} 

# 可以先判断，再删
if 'a' in s:
    s.remove('a')

# 也是删除元素，如果元素不存在，不会引发KeyError
s.discard('a')
print(s) # 输出: {'b', 'c', 'd', 'e', 'f', 'g', 'h'}

# 随机删除一个元素
print(s.pop()) 

# 清除元素
s.clear()
print(s) # 输出: set()


# 集合运算
# 集合的交集
s1 = set('abc')
s2 = set('cde')
print(s1.intersection(s2)) # 输出: {'c'}
print(s1 & s2) # 输出: {'c'}

# 集合的并集
print(s1.union(s2)) # 输出: {'a', 'b', 'c', 'd', 'e'}
print(s1 | s2) # 输出: {'a', 'b', 'c', 'd', 'e'}

# 集合的差集
print(s1.difference(s2)) # 输出: {'b', 'a'}
print(s1 - s2) # 输出: {'b', 'a'}

# 集合的对称差集
print(s1.symmetric_difference(s2)) # 输出: {'b', 'a', 'd', 'e'}
print(s1 ^ s2) # 输出: {'b', 'a', 'd', 'e'}

# 判断子集
print(s1.issubset(s2)) # 输出: False
print(s1 < s2) # 输出: False
print(s1 <= s2) # 真子集, 输出: False

# 判断两个集合有没有相同的元素, 有则返回False，没有则返回True
print(s1.isdisjoint(s2)) # 输出: False

# 判断超集
print(s1.issuperset(s2)) # 输出: False
print(s1 > s2) # 输出: False


# 集合的比较
s3 = set('abc')
print(s1 == s2) # 输出: False
print(s1 == s3) # 输出: True

# 集合长度
print(len(s1)) # 输出: 3

# 遍历集合
for e in s1:
    print(e)

# 集合转换为列表
s = set('abc')
l = list(s)
print(l) # 输出: ['a', 'b', 'c'], 顺序不定

# 集合转换为元组
s = set('abc')
t = tuple(s)
print(t) # 输出: ('a', 'b', 'c')

# 不可变类型的集合
s = frozenset('abc')
# s.add('d') # 报错，frozenset没有add方法
# s.remove('a') # 报错，frozenset没有remove方法