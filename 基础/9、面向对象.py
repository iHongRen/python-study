# 面向对象

# 类
# 使用 class 关键字定义类，这是一个空类
class MyClass:
    pass

# 实例化
my_instance = MyClass()
print(type(my_instance)) # 输出 <class '__main__.MyClass'>

# 实例属性、类属性
class MyClass:
    name3 = '我是类属性'

    # 构造函数 __init__()
    def __init__(self):
        self.name = 'public' # 公共属性
        self._name1 = 'protected' # 约定一个_开头的为保护属性, 允许其本身与子类进行访问
        self.__name2 = 'private' # 约定两个__开头的为私有属性, 类外不能直接访问

    def my_method(self):
        print(f"类内部可访问私有属性： {self.__name2}!")

m = MyClass()
print(m.name) # 输出: public
print(m._name1) # 输出: protected
# print(m.__name2) # 报错, 类外不能直接访问

# Python并没有严格保证私有属性的私密性，它只是给私有的属性和方法换了一个名字来阻挠对它们的访问
# 只要知道更换名字的规则，比如可以通过“_类名__属性名”来访问私有属性。私有方法也一样。
print(m._MyClass__name2) # 输出: private

# 类内部可访问私有属性
print(m.my_method()) # 输出: private!

# 类属性, 归类 MyClass 所有
print(MyClass.name3) # 输出: 我是类属性

# 实例对象找不到实例属性时，会去类属性中查找
print(m.name3) # 输出: 我是类属性



# 实例方法、类方法、静态方法
class MyClass:
    # self 表示实例对象本身, 也可以用其他名字代替, 比如下面的 self 可以用 this 代替
    def __init__(self, name):
        self.name = name

    def my_method(this, greet):
        print(f"{greet}, {this.name}!")

    # 这类 __foo__ 的方法一般是系统定义的名字, 通常不直接调用，而是重写
    #  __repr__() 会在 print 调用时调用
    def __repr__(self):
        return f"自定义打印：({self.name})"

    # 析构方法，对象销毁时调用
    def __del__(self):
        print(f"{self.name} 被销毁.")

    # 静态方法
    @staticmethod
    def my_static_method(str):
        print(f"static, {str}!")

    # 类方法, 比静态方法多一个 cls 参数, 表示类本身
    @classmethod
    def my_class_method(cls, str):
        print(f"{cls}, {str}!")

# 实例化
m = MyClass('cxy')
m.my_method('Hello') # 输出 Hello, cxy!
print(m) # 输出 自定义打印：(cxy)

# 调用静态方法
MyClass.my_static_method('cxy') # 输出 static, cxy!

# 调用类方法
MyClass.my_class_method('cxy') # 输出 <class '__main__.MyClass'>, cxy!


# 继承
# 格式 class SubClass(SuperClass1, SuperClass2, ...):
class SubClass(MyClass):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__weight = 0

    # 子类重写父类的方法
    def my_method(self, greet):
        print(f"{greet}, {self.name}, {self.age}!")

    # getter 方法, 用于获取属性值
    @property
    def weight(self):
        return self.__weight

    # setter 方法, 用于设置属性值
    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("体重不能为负数")
        self.__weight = value


sub = SubClass('cxy-sub', 18)
print(sub.name) # 输出: cxy-sub
sub.my_method('Hello') # 输出: Hello, cxy-sub, 18!
sub.weight = 60 # 调用 weight 的 setter
print(sub.weight) # 输出: 60


# 打印 sub 的所有属性
print(dir(sub))

# 判断 sub 是否有 weight 属性
print(hasattr(sub, 'weight')) # 输出: True

# 获取 sub 的 height 属性，没有就用默认 180
print(getattr(sub, 'height', 180)) # 输出: 180

# 判断 sub 是否是 SubClass 的实例
print(isinstance(sub, SubClass))

# 判断 sub 是否是 MyClass 的实例
print(isinstance(sub, MyClass))

# 判断 sub 是否是 object 的实例
print(isinstance(sub, object))

# 判断 SubClass 是否是 MyClass 的子类
print(issubclass(SubClass, MyClass))

# 判断 SubClass 是否是 object 的子类
# 所有类的根类都是 object
print(issubclass(SubClass, object))

# 获取 sub实例 的 hash 值
print(hash(sub))