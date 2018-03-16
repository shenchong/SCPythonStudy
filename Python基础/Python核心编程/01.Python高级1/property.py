# -*- coding: UTF-8 -*-

class Test2(object):
    def __init__(self):
        self.__obj = 10

    def setObj(self, newObj):
        self.__obj = newObj

    def getObj(self):
        return self.__obj
    obj = property(getObj,setObj)

t2 = Test2()
# t2.setObj(100)
# print(t2.getObj())
print(t2.obj) # 打印10

class Test3(object):
    def __init__(self):
        self.__obj = 10

    @property
    def obj(self):
        print("---getter---")
        return self.__obj

    @obj.setter
    def obj(self, newObj):
        print("---setter---")
        self.__obj = newObj

t3 = Test3()
t3.obj = 100
print(t3.obj)

# 打印结果，t3.obj = 100调用set方法，t3.obj调用get方法
# ---setter---
# ---getter---
# 100