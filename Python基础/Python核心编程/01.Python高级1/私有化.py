# -*- coding: UTF-8 -*-

class Test(object):
    def __init__(self):
        self.number = 100
        self.__number = 200
        print(id(self.number),id(self.__number))

t = Test()
print(t.number,id(t.number))
t.number = 101
t.__number = 201
print(t.number,id(t.number),t.__number,id(t.__number))


# 打印结果
# (140655527493280, 140655527496808)
# (100, 140655527493280)
# (101, 140655527493256, 201, 140655527496784)
# 原因是第一个t.number就是类init创建的，第二个t.number是给t对象重新创建赋值的，__number是私有的拿不到，外层的t.__number是重新创建赋值的

class Test2(object):
    def __init__(self):
        self.__obj = 10

    def setObj(self, newObj):
        self.__obj = newObj

    def getObj(self):
        return self.__obj

t2 = Test2()
t2.setObj(100)
print(t2.getObj())
# 写了个set和get方法，设置和取出私有属性