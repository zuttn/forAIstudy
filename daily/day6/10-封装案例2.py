# 作者: 王道 龙哥
# 2025年06月02日14时58分15秒
# xxx@qq.com
class Gun:

    def __init__(self, model):
        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 判断是否还有子弹
        if self.bullet_count <= 0:
            print("没有子弹了...")

            return

        # 发射一颗子弹
        self.bullet_count -= 1

        print("%s 发射子弹[%d]..." % (self.model, self.bullet_count))


class Soldier:

    def __init__(self, name):

        # 1. 姓名
        self.name = name

        # 2. 枪 - 新兵没有枪
        self.gun = None

    def fire(self):
        if self.gun is None:
            print('士兵没有枪')
            return
        print('冲啊')
        self.gun.add_bullet(50)
        # 4. 让枪发射子弹
        self.gun.shoot()


gun=Gun('AK47')
xusanduo=Soldier('许三多')
xusanduo.gun=gun
xusanduo.fire()

a=xusanduo
print(a is xusanduo) #判断两个对象是否执行同一个地方
