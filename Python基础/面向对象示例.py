# 设计4s店
# -*- coding: UTF-8 -*-

class CarStore(object):
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

car_store = CarStore()
car = car_store.order("朗逸")
car.move()
car.music()
car.stop()




		