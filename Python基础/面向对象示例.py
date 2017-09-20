# -*- coding: UTF-8 -*-

class Store(object):
    def select_car(self):
        pass

    def order(self, car_name):
        return self.select_car()


class BMWCarStore(Store):
    def __init__(self):
        self.factory = BMWFactory()

    def order(self, car_name):
        return self.factory.select_car_by_name(car_name)

# 使用函数将CarStore类解耦
class BMWFactory(object):
    def select_car_by_name(self, car_name):
        if car_name == "530Li":
            return Lavida()
        elif car_name == "mini":
            return Passat()
        elif car_name == "X6":
            return Magotan()

class DZCarStore(Store):
    def __init__(self):
        self.factory = Factory()

    def order(self, car_name):
        return self.factory.select_car_by_name(car_name)

# 使用函数将CarStore类解耦
class Factory(object):
    def select_car_by_name(self, car_name):
        if car_name == "朗逸":
            return Lavida()
        elif car_name == "帕萨特":
            return Passat()
        elif car_name == "迈腾":
            return Magotan()

class Car(object):
    def move(self):
        print("-- 车在移动 --")

    def music(self):
        print("-- 车在播放音乐 --")

    def stop(self):
        print("-- 停车 --")

class Lavida(Car):
    pass

class Passat(Car):
    pass

class Magotan(Car):
    pass

car_store = DZCarStore()
car = car_store.order("朗逸")
car.move()
car.music()
car.stop()


# 注：下面该模式为工厂方法模式，Store中order方法的self.select_car()，会调用子类中的方法
# -*- coding: UTF-8 -*-

class Store(object):
    def select_car(self):
        pass

    def order(self, car_name):
        return self.select_car(car_name)


class BMWCarStore(Store):

    def select_car(self, car_name):
        return BMWFactory.select_car_by_name(car_name)

# 使用函数将CarStore类解耦
class BMWFactory(object):
    @classmethod
    def select_car_by_name(self, car_name):
        if car_name == "530Li":
            return Lavida()
        elif car_name == "mini":
            return Passat()
        elif car_name == "X6":
            return Magotan()

class CarStore(Store):
    def select_car(self, car_name):
        return Factory.select_car_by_name(car_name)

# 使用函数将CarStore类解耦
class Factory(object):
    @classmethod
    def select_car_by_name(self, car_name):
        if car_name == "朗逸":
            return Lavida()
        elif car_name == "帕萨特":
            return Passat()
        elif car_name == "迈腾":
            return Magotan()

class Car(object):
    def move(self):
        print("-- 车在移动 --")

    def music(self):
        print("-- 车在播放音乐 --")

    def stop(self):
        print("-- 停车 --")

class Lavida(Car):
    pass

class Passat(Car):
    pass

class Magotan(Car):
    pass

car_store = CarStore()
car = car_store.order("朗逸")
car.move()
car.music()
car.stop()
