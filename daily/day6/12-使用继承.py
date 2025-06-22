# 作者: 王道 龙哥
# 2025年06月02日15时23分03秒
# xxx@qq.com
class Animal:

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

    def bark(self):
        print('汪汪叫--')


class XiaoTianQuan(Dog):
    def fly(self):
        print('飞----')

    def bark(self):
        #super匿名父类
        super().bark()
        print('像神一样的叫--')


# wangcai = Dog()
# wangcai.drink()

xiaotianquan = XiaoTianQuan()
xiaotianquan.bark()
