# 作者: 王道 龙哥
# 2025年06月02日10时49分41秒
# xxx@qq.com

#object 是基类，每一个类的父类
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print('run')

    def eat(self):
        print('eat')


class Dog:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def bark(self):
        pass

    def shake(self):
        pass

# 实例化
elephant = Person('大象', 18, 1.75)
tiger = Person('老虎', 17, 1.65)
print(elephant.name)  # 打印对象属性
elephant.run()  # 调用对象方法
