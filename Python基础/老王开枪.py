# -*- coding: UTF-8 -*-

class Person (object):
    """人的类"""
    def __init__(self, name):
        super(Person,self).__init__()
        self.name = name
        self.gun = None#用来保存对枪的引用
        self.hp = 100

    def install_bullet(self, dan_jia_temp, bullet_temp):
        """把子弹装到弹夹中"""

        #弹夹.保存子弹
        dan_jia_temp.storage_bullet(bullet_temp)

    def install_danjia(self, gun_temp, dan_jia_temp):
        """把弹夹安装到枪中"""
        #枪.保存弹夹(弹夹)
        gun_temp.storage_danjia(dan_jia_temp)

    def naqiang(self,gun_temp):
        """拿起一把枪"""
        self.gun = gun_temp

    def __str__(self):
        if self.gun:
            return "%s的血量为:%d, 他有枪 %s"%(self.name, self.hp, self.gun)
        else:
            if self.hp>0:
                return "%s的血量为%d, 他没有枪" % (self.name, self.hp)
            else:
                return "%s已挂"%(self.name)


    def kou_ban_ji(self,diren):
        """让枪发子弹打敌人"""
        self.gun.fire(diren)

    def diao_xue(self,sha_shang_li):
        self.hp -= sha_shang_li

class Gun(object):
    """枪的类"""
    def __init__(self, name):
        super(Gun,self).__init__()
        self.name = name #用来记录枪的类型
        self.danjia = None #用来记录弹夹对象的引用

    def storage_danjia(self, dan_jia_temp):
        """用一个属性保存弹夹对象的引用"""
        self.danjia = dan_jia_temp

    def __str__(self):
        if self.danjia:
            return "枪的信息为:%s, %s" % (self.name, self.danjia)
        else:
            return "枪的信息为:%s,这把枪中没有弹夹" % (self.name)
    def fire(self, diren):
        """开火"""
        #先从弹夹中取子弹
        bullet_temp = self.danjia.tanchu_bullet()

        #子弹击中敌人
        if bullet_temp:
            bullet_temp.dazhong(diren)
        else:
            print("弹夹没子弹了")

class Danjia (object):
    """弹夹的类"""
    def __init__(self, max_num):
        super(Danjia,self).__init__()
        self.max_num = max_num #用来记录弹夹的最大容量
        self.bullet_list = []#用来记录所有子弹的引用

    def storage_bullet(self, bullet_temp):
        """将子弹存储"""
        self.bullet_list.append(bullet_temp)

    def __str__(self):
        return "弹夹的信息为:%d/%d"%(len(self.bullet_list),self.max_num)

    def tanchu_bullet(self):
        """弹出最上面那颗子弹"""
        if self.bullet_list:
            return self.bullet_list.pop()
        else:
            return None

class Bullet (object):
    """子弹的类"""
    def __init__(self, sha_shang_li):
        super(Bullet,self).__init__()
        self.sha_shang_li = sha_shang_li

    def dazhong(self, diren):
        """让敌人掉血"""
        #敌人.掉血(一颗子弹的威力)
        diren.diao_xue(self.sha_shang_li)

def main():
    """主函数，用来控制整个程序的流程"""

    #1、创建一个老王对象
    laowang = Person("老王")

    #2、创建一个枪对象
    ak47 = Gun("AK47")

    #3、创建一个弹夹对象
    dan_jia = Danjia(20)

    #4、创建一些子弹
    for i in range(15):
        bullet = Bullet(10)
        #5、老王把子弹安装到弹夹中
        #老王.安装子弹到弹夹中(弹夹, 子弹)
        laowang.install_bullet(dan_jia, bullet)

    #6、老王把子弹安装到枪中
    #老王.安装弹夹到枪中(弹夹, 枪)
    laowang.install_danjia(ak47, dan_jia)

    #test: 测试弹夹的信息
    # print(dan_jia)

    #test: 测试枪的信息
    # print(ak47)

    #7、老王拿起枪
    #老王.拿枪(枪)
    laowang.naqiang(ak47)
    print(laowang)

    #8、创建一个敌人
    gebi_laosong = Person("隔壁老宋")
    print(gebi_laosong)

    #9、老王开枪打敌人
    #老王.扣扳机(隔壁老宋)
    laowang.kou_ban_ji(gebi_laosong)
    print(gebi_laosong)
    print(laowang)

if __name__ == '__main__':
    main()