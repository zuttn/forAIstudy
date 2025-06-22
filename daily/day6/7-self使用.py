# 作者: 王道 龙哥
# 2025年06月02日11时16分45秒
# xxx@qq.com
class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def run(self):
        print(f'{self.name} run')

    def eat(self):
        print('eat')


elephant = Person('大象', 18, 1.75)
# print(elephant.gender)
elephant.gender = True  #不要这么写
print(elephant.gender)
