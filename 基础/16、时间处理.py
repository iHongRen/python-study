# 时间处理

# Python 提供了三个与时间操作相关的模块：
# time 模块侧重于底层时间操作，时分秒
# datetime 模块侧重于处理日期，年月日时分秒
# calendar 模块侧重于处理日历，年月日、星期几等


# 时间的表示方式
# 在 Python 中，通常用这三种方式来表示时间：

# 时间戳（timestamp）通常来说，时间戳表示的是从 1970年1月1日00:00:00 开始按秒计算的偏移量，在 Python 中是一个浮点数。
# 格式化的时间字符串 ，比如 Thu Nov 29 20:50:50 CST 2018，用于人的解读。
# 元组格式，对应 C 语言中的 struct_time 数据结构，一共有 9 个元素。



# time 模块
import time

# 时间戳，从 1970年1月1日00:00:00 到现在的秒数
print(time.time()) # 输出: 1719833876.1931908

# UTC 时间
gmt = time.gmtime()  # 9个元素的元组
print(gmt) # 输出: time.struct_time(tm_year=2024, tm_mon=7, tm_mday=1, tm_hour=19, tm_min=37, tm_sec=56, tm_wday=0, tm_yday=1, tm_isdst=0)

# 本地时间
local = time.localtime()
print(local) # time.struct_time(tm_year=2024, tm_mon=7, tm_mday=28, tm_hour=17, tm_min=7, tm_sec=35, tm_wday=6, tm_yday=210, tm_isdst=0)

# 解析年月日
y, m, d, *_ = local
print(y, m, d) # 输出: 2024 7 1

# 本地时区
print(local.tm_zone) # CST: 中国标准时间(China Standard Time)

# 当地时区距离GMT的偏移秒数
print(time.timezone) # 输出: -28800

# 元组时间格式化 (时间元组 转 时间字符串)
print(time.strftime('UTC: %Y-%m-%d %H:%M:%S', gmt)) # 输出: UTC: 2024-07-01 11:59:56
print(time.strftime('本地: %Y-%m-%d %H:%M:%S', local)) # 输出: 本地: 2024-07-01 19:59:56
print(time.strftime('本地12小时制: %Y-%m-%d %l:%M:%S', local)) # 输出: 本地12小时制: 2024-07-01 7:59:56

# 时间字符串 转 时间元组
time1 = time.strptime('2024-07-01 19:59:56', '%Y-%m-%d %H:%M:%S')
print(time1)
print(time.strftime("time1: %Y-%m-%d %H:%M:%S", time1))

# 时间元组 转 时间戳
timestamp = time.mktime(time1)
print(timestamp)

# 时间戳 转 时间元组
time2 = time.localtime(timestamp)
print(time2)
print(time.strftime("time2: %Y-%m-%d %H:%M:%S", time2))





# datetime 模块
from datetime import datetime

now = datetime.now() # 获取当前datetime
print(now) # 输出: 2024-07-01 20:29:39.486813

# 获取时间戳
print(now.timestamp()) # 输出: 1719833879.0

# 时间戳 转 时间
time3 = datetime.fromtimestamp(now.timestamp())
print(time3) # 输出: 2024-07-01 20:29:39.486813

# 时间字符串 转 时间
time4 = datetime.strptime('2024-07-01 20:29:39', '%Y-%m-%d %H:%M:%S')
print(time4) # 输出: 2024-07-01 20:29:39

# 时间 转 时间字符串
print(time4.strftime('%Y-%m-%d %H:%M:%S')) # 输出: 2024-07-01 20:29:39




# calendar 模块
import calendar

# 获取某月日历
print(calendar.month(2024, 7)) 
# 输出: 
#      July 2024
# Mo Tu We Th Fr Sa Su
#  1  2  3  4  5  6  7
#  8  9 10 11 12 13 14
# 15 16 17 18 19 20 21
# 22 23 24 25 26 27 28
# 29 30 31

# 获取某一天是周几, (0-6 ~ Mon-Sun)
print(calendar.weekday(2024, 7, 1))
# 输出: 0 , 表示周一

# 获取某月第一天是星期几以及该月有多少天
print(calendar.monthrange(2024, 7)) # 输出: (0, 31)

# 获取当天
today = calendar.datetime.date.today()
print(today)
print(today.year) # 输出: 2024
print(today.month) # 输出: 7
print(today.day) # 输出: 1
