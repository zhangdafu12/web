# -*- encoding:utf8 -*-
# author: Shulei
# e-mail: 1191543592@qq.com
# time:  2019/4/2 10:00
import time

# 一个描述器就是一个实现了三个核心的属性访问操作（get、set、delete）的类，分别为__get__(), __set__(),__delete__()
# 这些方法接受一个实例作为输入，之后相应的操作实例底层的字典, 为了使用一个描述器，需要将这个描述器的实例作为类属性放到一个类的定义中Dadej

# Descriptors are class attributes (like properties or methods) with any of the following special methods:
# __get__ (non-data descriptor method, for example on a method/function)
# __set__ (data descriptor method, for example on a property instance)
# __delete__ (data descriptor method)


class Celsius:
    def __init__(self, value=0.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        print(instance)
        print(owner)
        print("执行的是get")
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)

    def __delete__(self, instance):
        print("删除。。。。")
        print(self)
        print(instance)
        print(instance.__dict__)


class Temperature:
    celsius = Celsius()


t = Temperature()

print(t.celsius)
del t.celsius
print(t.celsius)

print(__name__)
if __name__ == '__main__':
    print("这里执行了")