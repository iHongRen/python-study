# 字符串 str

# 在 Python 中，字符串是以单引号或双引号或三引号引起来的。
s0 = 'hello'
print(type(s0))  # 输出: <class 'str'>

s1 = "world"
s2 = '''
hello
world
aaa
bbb
'''

# 原始字符串，以 r 开头，不会发生转义
s3 = r'hello \n world'
print(s3) # 输出：hello \n world

# 字符串拼接
s5 = s1 + s2
s6 = '11' + ' ' + '22'
print(s5) # 输出: helloworld
print(s6) # 输出: 11 22

s5 += s5 # 字符串拼接
s6 *= 2 # 字符串重复
print(s5) # 输出: helloworldhelloworld
print(s6) # 输出: 11 2211 22

s7 = 'a' * 10
print(s7) # 输出: aaaaaaaaaa

# 比较内存地址
print(s1 is s2) # 输出: False

# in 和 not in
print('hello' in s2) # 输出: True
print('hello' not in s2) # 输出: False

# 字符串长度
length = len(s2) 
print(length) # 输出: 21

# 字符串切片
s8 = '012345678'
print(s8[0])   # 第 0 个， 输出: 0
print(s8[0:5]) # 从 0 开始，到 5 结束，不包括 5, 输出: 01234
print(s8[6:])  # 从 6 开始，到结尾, 输出: 678
print(s8[:6])  # 从 0 开始，到 6 结束，不包括 6, 输出: 012345
print(s8[::2]) # 从 0 开始，到 结尾，步长为 2, 输出: 02468
print(s8[::-1]) # 从结尾开始，到 0 结束，步长为1, 输出: 876543210
print(s8[::-2]) # 从结尾开始，到 0 结束，步长为2, 输出: 86420

# 字符串遍历
for c in s1:
    print(c)

for i in range(len(s1)):
    print(s1[i])

# 字符串一些方法
s9 = 'hello world'
print(s9.upper()) # 全部大写, 输出: HELLO WORLD
print(s9.lower()) # 全部小写, 输出: hello world
print(s9.capitalize()) # 首字母大写, 输出: Hello world
print(s9.title()) # 首字母大写, 输出: Hello World
print(s9.swapcase()) # 大小写翻转, 输出: HELLO wORLD

print(s9.count('l')) # 统计 'l' 出现的次数, 输出: 3
print(s9.find('l')) # 查找 'l' 的位置，找不到返回 -1, 输出: 2
print(s9.rfind('l')) # 反向查找 'l' 的位置，找不到返回 -1, 输出: 9

print(s9.index('l')) # 查找 'l' 的位置，找不到会报错, 输出: 2
print(s9.rindex('l')) # 反向查找 'l' 的位置，找不到会报错, 输出: 9

print(s9.center(20)) # 居中，长度为 20，用空格填充, 输出:     hello world
print(s9.center(20, '*')) # 居中，长度为 20，用 '*' 填充，输出: ****hello world*****
print(s9.ljust(20)) # 左对齐，长度为 20，用空格填充, 输出: hello world     
print(s9.ljust(20, '*')) # 左对齐，长度为 20，用 '*' 填充，输出: hello world*********
print(s9.rjust(20)) # 右对齐，长度为 20，用空格填充, 输出:          hello world
print(s9.rjust(20, '*')) # 右对齐，长度为 20，用 '*' 填充, 输出: *********hello world
print(s9.zfill(20)) # 左对齐，长度为 20，用 '0' 填充，输出: 000000000hello world

print(s9.startswith('He')) # 判断是否以 'He' 开头, 输出: False
print(s9.startswith('hel')) # 判断是否以 'hel' 开头, 输出: True
print(s9.endswith('d')) # 判断是否以 'd' 结尾, 输出: True

s10 = '123456'
print(s10.isalpha()) # 判断是否全为字母, 输出: False
print(s10.isdigit()) # 判断是否全为数字, 输出: True
print(s10.isalnum()) # 判断是否全为字母或数字, 输出: True
print(s10.isdecimal()) # 判断是否全为十进制数字, 输出: True
print(s10.isspace()) # 判断是否全为空白字符, 输出: False
print(s10.isnumeric()) # 判断是否全为数字, 输出: True
print(s10.isascii()) # 判断是否全为 ASCII 字符, 输出: True


# 格式化
a = 10
b = 20
print('%d + %d = %d' % (a,b, a+b)) # 输出: 10 + 20 = 30
print('{} * {} = {}'.format(a,b, a*b)) # 输出: 10 * 20 = 200
print(f'{a} / {b} = {a/b}') # 输出: 10 / 20 = 0.5

# 去掉空格
s11 = '  hello  '
print(s11.strip()) # 去掉两边的空格, 输出: hello
print(s11.lstrip()) # 去掉左边的空格, 输出: hello   
print(s11.rstrip()) # 去掉右边的空格, 输出:  hello

# 替换
print(s11.replace('hello', 'world')) # 全部替换, 输出:   world
print(s11.replace('hello', 'world', 1)) # 第三个参数指定替换的次数, 输出:  world

# 分割/合并
print(s11.split(' ')) # 按空格分割, 输出: ['', 'hello', '', '']
print(' '.join(['hello', 'world', 'aaa', 'bbb'])) # 按空格合并, 输出: hello world aaa bbb

# 编码和解码
# 编码和解码的方式不一致，会导致乱码
s12 = '中'
print(s12.encode('gbk')) # 输出: b'\xd6\xd0'
s13 = s12.encode('utf-8') 
print(s13) # 输出: b'\xe4\xb8\xad'
print(s13.decode('utf-8')) # 输出: 中

print(ord(s12)) # 打印码点 输出：20013
print(chr(20013)) # 码点对应的字符 输出：中

print(hex(ord(s12))) # 打印码点的十六进制 输出：0x4e2d
print(chr(0x4e2d)) # 十六进制对应的字符 输出：中
print('\u4e2d') # 直接打印 Unicode 字符 输出：中