# 枚举

# 枚举是一组相关值的集合
# 枚举成员应该是唯一的、不可变的
# 枚举提高了代码的可读性、可维护性、可靠性

from enum import Enum

# 使用继承的方式, 定义枚举
class RequestType(Enum):
    GET = 1
    POST = 2

print(type(RequestType)) # 输出: <class 'enum.EnumType'>
print(RequestType.GET) # 输出: RequestType.GET
print(RequestType.GET.value) # 成员值, 输出: 1
print(RequestType.GET.name) #  成员名 输出: GET


# 或者, 使用 Enum 类直接定义枚举
Direction = Enum('Direction', 'TOP BOTTOM LEFT RIGHT')

# 遍历枚举
for item in Direction:
    print(item)
# Direction.TOP
# Direction.BOTTOM
# Direction.LEFT
# Direction.RIGHT

for name, member in Direction.__members__.items():
    print(name, member)
# TOP Direction.TOP
# BOTTOM Direction.BOTTOM
# LEFT Direction.LEFT
# RIGHT Direction.RIGHT

# 枚举比较
print(RequestType.GET == RequestType.POST) # 输出: False
print(Direction.TOP == Direction.TOP) # 输出: True

# 不支持大小比较
# print(RequestType.POST > RequestType.GET) 
# 输出: TypeError: '>' not supported between instances of 'RequestType' and 'RequestType'


# 派生的枚举 IntEnum
# IntEnum 也是 int 的一个子类， IntEnum 的成员可与整数进行比较
from enum import IntEnum
class Color(IntEnum):
    RED = 1
    GREEN = 2

print(Color.RED == 1) # 输出: True
print(Color.RED < Color.GREEN) # 输出: True

# 派生的枚举 StrEnum
# StrEnum 也是 str 的一个子类， StrEnum 的成员可与字符串进行比较
from enum import StrEnum
class Fruit(StrEnum):
    APPLE = "apple"
    BANANA = "banana"

print(Fruit.APPLE == "apple") # 输出: True
print(Fruit.APPLE > Fruit.BANANA) # 输出: False


# 派生的枚举 Flag
# 成员可使用按位运算，类似其他语言的 选项枚举
# 使用 auto 自动设定的值
from enum import Flag, auto
class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

print(Color.RED | Color.GREEN) # 输出: Color.RED | Color.GREEN
print(Color.BLUE.value) # 输出: 4


# 默认情况下，枚举成员的值是可以重复的
# 使用 unique 确保枚举值唯一
from enum import Enum, unique

@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # BLACK = 1  ValueError: duplicate values found in <enum 'Color'>: BLACK -> RED
