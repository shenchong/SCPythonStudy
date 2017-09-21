# -*- coding: UTF-8 -*-
# 单例的创建

# class Dog(object):
#     __instance = None
#     def __new__(cls):
#         if cls.__instance == None:
#             cls.__instance = object.__new__(cls)
#             return cls.__instance
#         else:
#             return cls.__instance
#
# a = Dog()
# print(id(a))
# b = Dog()
# print(id(b))

class Dog(object):
    __instance = None
    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        self.name = name

a = Dog("dongsi")
print(id(a), a.name)
b = Dog("wangcai")
print(id(b), b.name, a.name) # 这里a.name也会打印"wangcai"，原因是cls只初始化一次，self指向地址不变。


# 打印结果：
(4456063760, 'dongsi')
(4456063760, 'wangcai', 'wangcai')

