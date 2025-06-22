# 作者: 王道 龙哥
# 2025年06月02日16时05分13秒
# xxx@qq.com
class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print("吃---")

    def drink(self):
        print("喝---")

    def run(self):
        print("跑---")

    def sleep(self):
        print("睡---")


class Dog(Animal):

# 子类重写父类的init
    def __init__(self, name, color):
        super().__init__(name)      # 执行父亲的init，初始化了孩子对象的属性
        self.color=color

    def bark(self):
        print('汪汪叫--')


wangcai = Dog('旺财', '黄色')
print(wangcai.name)
print(wangcai.color)