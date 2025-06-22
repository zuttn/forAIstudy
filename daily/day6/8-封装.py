# 作者: 王道 龙哥
# 2025年06月02日14时34分17秒
# xxx@qq.com
class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def run(self):
        print(f'{self.name} run')
        self.weight -= 0.5

    def eat(self):
        print(f'{self.name} eat')
        self.weight += 1

    def __str__(self):
        return f'{self.name} 体重是{self.weight}'


elephant = Person('大象', 18, 1.75, 75)
elephant.run()
print(elephant)
elephant.eat()
print(elephant)

